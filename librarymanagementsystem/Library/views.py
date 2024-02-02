from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from rest_framework.decorators import api_view,parser_classes,authentication_classes,permission_classes
from .serializers import LoginSerializer,StudentSerializer,BookSerializer
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Student




@api_view(['POST'])
def login_user(request):
    user=get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error":"Invalid Password"},status=status.HTTP_404_NOT_FOUND)
    token,create=Token.objects.get_or_create(user=user)
    serializer=LoginSerializer(user)
    return Response({'token':token.key,"user":serializer.data},status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def list_students(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([FormParser,MultiPartParser])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def add_student(request):
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Student added to database"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def get_student_id(request,pk):
    student=get_object_or_404(Student,UserID=pk)
    serializer=StudentSerializer(student)
    return Response(serializer.data,status=status.HTTP_200_OK)




@api_view(['POST'])
@parser_classes([FormParser,MultiPartParser])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def add_book(request):
    if request.method=="POST":
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Book added to database"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    






