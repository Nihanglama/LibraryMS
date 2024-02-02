from django.urls import path
from .views import login_user,add_student,get_student_id,list_students,add_book


urlpatterns=[
    path('api/login',login_user,name='login'),
    path('api/list_student',list_students,name='liststudent'),
    path("api/add_student",add_student,name="addstudent"),
    path("api/get_student/<int:pk>",get_student_id,name="getstudent"),
    path("api/add_book",add_book,name="addbook")
]