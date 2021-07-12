# Basketball League API using Django REST framework :basketball: :basketball_man: 
## Introduction
This is an API regarding basketball league to develop a management system to monitor games statistics and rankings.

## Setup
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

### Access Levels 

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

## APIs

Use the following URLs to access the APIs
## GET
NOTE: Pass the logged user's token inside the header under "Authorization" key. As shown in the blow images.

(format: Token 9666677f6421bf89feb1b7121fd9ea8096fbee66)
##### View the scoreboard
```
http://localhost:8000/api/match_details
```
![image](https://user-images.githubusercontent.com/20280857/125286580-9822f180-e339-11eb-86c6-e1e214e5f374.png)


##### View the team players
```
http://localhost:8000/api/team_players
```
![image](https://user-images.githubusercontent.com/20280857/125286677-b8eb4700-e339-11eb-9f48-8cf4bd373f0a.png)


##### View player details
```
http://localhost:8000/api/player/1
```
![image](https://user-images.githubusercontent.com/20280857/125286789-d3252500-e339-11eb-8c59-afbc0b9af762.png)


#### View top players with ranks
```
http://localhost:8000/api/top_players
```
![image](https://user-images.githubusercontent.com/20280857/125286910-efc15d00-e339-11eb-8720-bdaa1f26a1d4.png)



## POST

##### Login
```
http://localhost:8000/api/login
```
![image](https://user-images.githubusercontent.com/20280857/125284961-b556c080-e337-11eb-8440-0f5409b127b4.png)

##### Logout
```
http://localhost:8000/api/logout
```
![image](https://user-images.githubusercontent.com/20280857/125285125-f18a2100-e337-11eb-9a49-601004023060.png)


Results may change according to the user's access level.


  
