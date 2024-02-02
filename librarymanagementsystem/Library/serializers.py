from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student,Book,BookDetail,BorrowedBook


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password')


class StudentSerializer(serializers.ModelSerializer):
    UserID=serializers.IntegerField(read_only=True)

    class Meta:
        model=Student
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    BookID=serializers.IntegerField(read_only=True)
    class Meta:
        model=Book
        fields="__all__"






