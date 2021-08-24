# Django_final_project
Final django project from django backend bootcamp 

## Summary
Django LFG Wep API for Company employees to be able to connect with some others according to videgames likes, to have time together afterwork.

In this App a user can generate new videogames and party groups related to such videogame. 
Also he/she can search for already generated party groups per each videogame and leave any comments on it.
Any user can generate, edit and/or delete any of his/her onw generated videogames, parties and, of course, his/her own party messages, 
but only read the rest of the videogame list, parties and messages, generated but the rest of the users.

Also on /users/ a user can see the complete list of the usersin where they can check for their particular profile and go and edit it, by including fileds like;
steam user and/or preferred social network link.

## Tecnology stack used:
* Python (OOP)
* Django
* Django Rest Framework
* PostgreSQL
* VirtualENV
* JWT
* Git-Gitflow

## Objectives accomplished
* User register
* User login/logout
* User edit profile (with extra fields)
* Complete CRUD for videogames, party groups and party messages
* Read permissions for user generated objects not for current user

## Requirements
* python              3.8.10
* Django              3.2.5
* django-allauth      0.44.0
* django-filter       2.4.0
* django-rest-auth    0.9.5
* djangorestframework 3.12.4
* oauthlib            3.1.1
* psycopg2            2.9.1
