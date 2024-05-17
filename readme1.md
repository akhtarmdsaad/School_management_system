# Student Management System Created Using Django
This is a Simple Student Management System Developed While Learning Django.
Feel free to make changes based on your requirements.


And if you like this project, then ADD a STAR ⭐️  to this project 👆



## Features of this Project

### A. Admin Users Can :
1. See Overall Summary Charts of Students Performances, Staff Performances, Courses, Subjects, Leave, etc.
2. Manage Staff (Create, Read, Update and Delete)
3. Manage Students (Create, Read, Update and Delete)
4. Manage Course (Create, Read, Update and Delete)
5. Manage Subjects (Create, Read, Update and Delete)
6. Manage Sessions (Create, Read, Update and Delete)
7. View Student Attendance
8. Review and Reply Student/Staff Feedback
9. Review, Approve or Reject Student/Staff Leave
10. Send Notifications to Student/Staff

### B. Staff/Teachers Can :
1. See the Overall Summary Charts related to their students, their subjects, leave status, etc.
2. Take/Update Students Attendance
3. Add/Update Result
4. Apply for Leave
5. Send Feedback to HOD
6. View Notifications

### C. Students Can :
1. See the Overall Summary Charts related to their attendance, their subjects, leave status, etc.
2. View Attendance
3. View Result
4. Apply for Leave
5. Send Feedback to HOD
6. View Notifications


## Support Developer
1. Add a Star 🌟  to this 👆 Repository
2. Follow me on Github

## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/jobic10/student-management-using-django.git
```

Then, Enter the project
```
$  cd student-management-using-django
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Add the hosts**

- Go to settings.py file 
- Then, On allowed hosts, Use **[]** as your host. 
```python
ALLOWED_HOSTS = []
```
*Do not use the fault allowed settings in this repo. It has security risk!*

**6. Make necessary Tables in Data**  
- Go to the terminal  
- Run the command

Command for Windows:
```python
$ python manage.py makemigrations
$ python manage.py migrate
```

Command for Mac:
```python
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Command for Linux:
```python
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```


**7. Login Credentials**

Create Super User (HOD)
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```


**8. Now Run Server**

Command for Windows:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

Then provide the required inputs to create superuser.

You are done. Have Fun!! 

