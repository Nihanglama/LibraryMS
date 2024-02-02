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

class BookDetailSerializer(serializers.ModelSerializer):
    DetailsID=serializers.IntegerField(read_only=True)
    class Meta:
        model=BookDetail
        fields = ['DetailsID', 'NumberOfPages', 'Publisher', 'Language']

class GetBookSerializer(serializers.ModelSerializer):
    book_details=BookDetailSerializer(many=True,read_only=True)
    class Meta:
        model=Book
        fields=['BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre','book_details']



class GetBorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowedBook
        fields=['UserID','BookID','BorrowDate','ReturnDate']

class BorrowedBookSerializer(serializers.ModelSerializer):
    UserID=serializers.IntegerField(read_only=True)
    BookID=serializers.IntegerField(read_only=True)
    class Meta:
        model=BorrowedBook
        fields=["UserID","BookID","ReturnDate"]