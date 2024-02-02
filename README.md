# LibraryMS
Python Intership application process Assignment


Steps to setup project
- create virtual environment 
-activate virtual environment (source youenvname/bin/activate)
- fire command "pip install -r requirements.txt"
- cd into project folder i.e librarymanagementsystem (cd librarymanagementsystem)
- fire command "python manage.py makemigrations"
- fire command "python manage.py migrate"
- fire command "python manage.py createsuperuser"  (only usersuperuser can login to system )
- fire command "python manage.py runserver"

API documentation

- "http://127.0.0.1:8000/admin"                         : For accessing Django Admin site (login with superuser username and password)

- "http://127.0.0.1:8000/api/login"                     : Login with username and password (keep the token ) 

- "http://127.0.0.1:8000/api/list_student "             : endpoints to list student

- "http://127.0.0.1:8000/api/add_student"               : endpoints to add student

- "http://127.0.0.1:8000/api/get_student/<int:pk>"      : endpoints to get student by id 

- "http://127.0.0.1:8000/api/add_book"                  : endpoints to add book

- "http://127.0.0.1:8000/api/get_book/<int:pk>"         : endpoints to get book by id 

- "http://127.0.0.1:8000/api/list_book"                 : list all available book

- "http://127.0.0.1:8000/api/update_book/<int:pk>"      : update book by id 

- "http://127.0.0.1:8000/api/update_book_details/<int:pk>" : update book details by bookid

- "http://127.0.0.1:8000/api/borrow_book "                 : borrow_book(provide book_id,student_id as input )

- "http://127.0.0.1:8000/api/list_borrowed_book"           : list all borrowed books 

- "http://127.0.0.1:8000/api/return_book "                 : return_book provide book_id,student_id and ReturnDate as input 


Note: use Token "your token "  in Authorization header while sending request to above endpoints since only admin user can perform all the above task. But json input and form inputs are supported for post,put requests


