from django.urls import path
from .views import login_user,add_student,get_student_id,list_students,add_book,get_book,list_books,update_book,borrow_book,list_borrow_book,return_book,update_book_details,list_api


urlpatterns=[
    path('',list_api),
    path('api/login',login_user,name='login'),
    path('api/list_student',list_students,name='liststudent'),
    path("api/add_student",add_student,name="addstudent"),
    path("api/get_student/<int:pk>",get_student_id,name="getstudent"),
    path("api/add_book",add_book,name="addbook"),
    path("api/get_book/<int:pk>",get_book,name="getbook"),
    path("api/list_book",list_books,name="listbook"),
    path("api/update_book/<int:pk>",update_book,name="updatebook"),
    path("api/update_book_details/<int:pk>",update_book_details,name="updatedetails"),
    path("api/borrow_book",borrow_book,name="borrowbook"),
    path("api/list_borrowed_book",list_borrow_book,name="listborrowedbook"),
    path("api/return_book",return_book,name="returnbook") 

]