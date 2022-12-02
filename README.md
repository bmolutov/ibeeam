# Project for discipline "Backend for high loaded environment"
## Developers<br/> 
Imangali Zhumash<br/> Bekzat Molutov<br/> Magzhan Zhumabekov

# Quick start
## Ibeeam microservice
It stands for main part of the application.<br/>
Go to ibeeam directory then:<br/>
to run Celery: <code>python -m celery -A django_celery worker -l info</code><br/>
to run Redis server: <code>redis-server</code><br/>
to run Django dev server: <code>python manage.py runserver</code><br/>

## Auxiliary microservice
It stands for high loaded part of the application.<br/>
Go to auxiliary directory then:<br/>
to run FastAPI dev server: <code>uvicorn main:app --reload --host 127.0.0.1 --port 8001</code><br/>
to run with environment variables: <br/>
<code>DEBUG=1 MAIN_SERVICE_URL_DEV="" MAIN_SERVICE_URL_PROD="" uvicorn main:app --reload --host 127.0.0.1 --port 8001</code>

## Setup for running project
1) Request init.sql file and put it into Docker/ directory
2) Request .env file and put it into ibeeam/ directory near settings.py file
The files are hidden for security purposes
If you have questions, please contact with Bekzat Molutov

## Running commands
We have created Makefile for defining aliases for django, postgres, docker, docker-compose commands

Use 'make' for performing commands. Firstly run 'make help' command to see documentation

# Extra info
We are following declarative approach using docker-compose.yml file, instead of imperative (when just manually running of commands is used).

We use .env file for holding environment variables for both services.

Our application consists of the following docker services: db, web. 

- db stands for our database (PostgreSQL of version 12.11 is used)
- web stands for our django application (Django of version 3.2.15 is used)

As you can see these services will run on different containers.

We have defined volumes for each service, there will be located files and data generated by runtime of the app.
Also these services are bound to one network with Bridge driver, which allows containers communicate with each other.

## Django app services
Here are the django app services that wer are going to implement and support:
1) Authentication/Authorization 
2) Commenting system
3) Posting articles
4) Search system
5) Search history system
6) Post author profile service 
7) Post/Comment reactions service
8) Following user
9) Blocking user
10) Favorites
 
## FastAPI part
it's empty here for now :)
