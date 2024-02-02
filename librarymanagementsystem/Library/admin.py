from django.contrib import admin
from .models import Student,Book,BookDetail,BorrowedBook

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(BookDetail)
admin.site.register(BorrowedBook)