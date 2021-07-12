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

## Features
There are three types of users.
  1. Admin
  2. Coach
  3. Player

Use following URLs to access APIs
#### GET
```
http://localhost:8000/api/match_details
http://localhost:8000/api/team_players
http://localhost:8000/api/player/1
http://localhost:8000/api/top_players
```
#### POST
```
http://localhost:8000/api/login
http://localhost:8000/api/logout
```

Results may change according to the user's access level.

## Access Levels 

Function\Levels | Admin | Coach | Player 
--- | --- | --- | --- 
Login to the site and logout | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:
--- | --- | --- | --- 
View the scoreboard | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:
--- | --- | --- | --- 
View list of players inside the team | :heavy_check_mark: | :heavy_check_mark: | :x:
--- | --- | --- | --- 
View player details in side the team | :heavy_check_mark: | :heavy_check_mark: | :x:
--- | --- | --- | --- 
View the players whose average score is above 90 with ranks | :heavy_check_mark: | :heavy_check_mark: | :x:
--- | --- | --- | --- 
View all the players in side the league | :heavy_check_mark: | :x: | :x: 
--- | --- | --- | --- 
View all the details of the players in side the league | :heavy_check_mark: | :x: | :x:
  
