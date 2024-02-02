from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ..models import Student, Book, BorrowedBook

class ViewsTestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='adminuser', password='adminpass', email='admin@example.com')
        self.token = Token.objects.create(user=self.admin_user)
        self.student = Student.objects.create(Name='Subash', Email='subash@test.com')
        self.book = Book.objects.create(Title='BuildwithDjango', ISBN='1234567890121', PublishedDate="2023-12-01", Genre="Educational")
        self.borrowed_book = BorrowedBook.objects.create(UserID=self.student, BookID=self.book)

    def authenticate_user(self):
        url = reverse('login')
        data = {'username': 'adminuser', 'password': 'adminpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['token']

    def test_list_students(self):
        url = reverse('liststudent')
        token = self.authenticate_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming you have one student in the database

    def test_add_student(self):
        url = reverse('addstudent')
        token = self.authenticate_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        data = {'Name': 'NewStudent', 'Email': 'newstudent@test.com'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)  # Assuming you had one student before the test

    def test_get_student_id(self):
        url = reverse('getstudent', args=[self.student.UserID])
        token = self.authenticate_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Name'], 'Subash')
        self.assertEqual(response.data['Email'], 'subash@test.com')


    def test_borrow_book(self):
        url = reverse('borrowbook')
        token = self.authenticate_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        data = {'student_id': self.student.UserID, 'book_id': self.book.BookID}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BorrowedBook.objects.count(), 2) 

    def test_list_borrow_book(self):
        url = reverse('listborrowedbook')
        token = self.authenticate_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    def test_add_book(self):
        url = reverse('addbook')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        data = {'Title': 'New Book', 'ISBN': '9876543210987', "PublishedDate":"2023-12-01", "Genre":"Educational"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book(self):
        url = reverse('getbook', kwargs={'pk': self.book.BookID})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')       

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_books(self):
        url = reverse('listbook')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

