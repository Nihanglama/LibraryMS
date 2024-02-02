from django.db import models


class Student(models.Model): # insted of User here I gave model name to Student 
    UserID=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Title

class BookDetail(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    BookID = models.ForeignKey(Book,related_name='book_details', on_delete=models.CASCADE)
    NumberOfPages = models.PositiveIntegerField(default=0)
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.BookID.Title

class BorrowedBook(models.Model):
    UserID= models.ForeignKey(Student, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField(auto_now_add=True)
    ReturnDate = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.UserID.Name




