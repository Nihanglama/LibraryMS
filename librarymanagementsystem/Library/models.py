from django.db import models


class Student(models.Model): # insted of User here I gave model name to Student 
    UserID=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField(auto_now_add=True)

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

class BookDetail(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    Book = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.PositiveIntegerField()
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)

class BorrowedBook(models.Model):
    UserID= models.ForeignKey(Student, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)




