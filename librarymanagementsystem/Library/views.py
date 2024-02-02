from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from rest_framework.decorators import api_view,parser_classes,authentication_classes,permission_classes
from .serializers import LoginSerializer,StudentSerializer,BookSerializer,GetBookSerializer,BookDetailSerializer,GetBorrowedBookSerializer,BorrowedBookSerializer
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Student,Book,BookDetail,BorrowedBook
from django.utils import timezone


@api_view(["GET"])
def list_api(request):
    endpoints=[
    "admin",
    "api/login",
    "api/list_student ",
    "api/add_student" ,
    "api/get_student/<int:pk> ",
    "api/add_book" ,
    "api/get_book/<int:pk> ",
    "api/list_book",
    "api/update_book/<int:pk> ",
    "api/update_book_details/<int:pk>",
    "api/borrow_book ",
    "api/list_borrowed_book",
    "api/return_book ",
    ]
    return Response({"available endpoints":endpoints})

@api_view(['POST'])
@parser_classes([FormParser,MultiPartParser,JSONParser])
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
@parser_classes([FormParser,MultiPartParser,JSONParser])
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
@parser_classes([FormParser,MultiPartParser,JSONParser])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def add_book(request):
    if request.method=="POST":
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Book added to Library"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def get_book(request,pk):
    book=get_object_or_404(Book,BookID=pk)
    serializer=GetBookSerializer(book)
    return Response(serializer.data,status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def list_books(request):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['PUT'])
@parser_classes([FormParser,MultiPartParser,JSONParser])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def update_book(request,pk):
    book=get_object_or_404(Book,BookID=pk)
    serializer=BookSerializer(book,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Information has been updated"})
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
@parser_classes([FormParser,MultiPartParser,JSONParser])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def update_book_details(request,pk):
    book=get_object_or_404(Book,BookID=pk)
    details_instance, created = BookDetail.objects.get_or_create(BookID=book)
    serializer=BookDetailSerializer(details_instance,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Information has been updated"})
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@parser_classes([FormParser,MultiPartParser,JSONParser])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def borrow_book(request):
    book_id=request.data['book_id']
    user_id=request.data['student_id']
    book=get_object_or_404(Book,BookID=book_id)
    student=get_object_or_404(Student,UserID=user_id)
    date=timezone.now().date()
    BorrowedBook.objects.create(
            UserID=student,
            BookID=book,
            BorrowDate=date,
        )
    return Response({"message:Book":"Book borrowed"},status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def list_borrow_book(request):
    borrowed_book=BorrowedBook.objects.all()
    print(borrowed_book)
    serializer=GetBorrowedBookSerializer(borrowed_book,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['PUT'])
@parser_classes([FormParser,MultiPartParser,JSONParser])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([SessionAuthentication,TokenAuthentication])
def return_book(request):
    book_id=request.data['book_id']
    user_id=request.data['student_id']
    borrowed_book=get_object_or_404(BorrowedBook,UserID=user_id,BookID=book_id)
    serializer=BorrowedBookSerializer(borrowed_book,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Book has been returned by User"},status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    

    


    


    
    





    
    










