# Basketball League API using Django REST framework :basketball: :basketball_man: 
## Introduction
This is an API regarding basketball league to develop a management system to monitor games statistics and rankings.

## Installation
1. The first thing to do is to clone the repository
```
$ git clone https://github.com/Nilansha/basketball-league-django-rest-api.git
$ cd basketball-league-django-rest-api
```

2. If you are using PyCham set Django server configurations (virtual enviorenment and etc). 
3. Open your terminal and run these to perform the initial database migration. You will only need to run this the very first time you deploy your app until you change the db models.
```
python manage.py makemigrations
python manage.py migrate
``` 

4. And navigate to http://127.0.0.1:8000/admin/ check your project.
5. Use postman to access APIs.
