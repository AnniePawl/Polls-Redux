
1. Check version of Django 
- `$ python -m django --version` 

2. Auto generate code to establish Django project 
- `$ django-admin startproject mysite` 

3. Put code somewhere outside document room like, home/mycode

4. Start Django development server, lightweight web server 
- Development servere auto reloads code for each request as needed
- `$ python manage.py runserver`

5. Create apps within project
-  Make sure you are in same directory as manage.py
- `$python3 manage.py startapp app name`

6. Creates tables in database
- `$python manage.py migrate`

7. Include app in project by refererncing config class in INSTALLED_APP setting 
- `$python3 manage.py makemigrations polls(app)`

8. Create an Admin User
- `$python3 manage.py createsuperuser`

- `python manage.py check` checks for any problems in project without making migrations or touching db

- `$ python manage.py sqlmigrate polls 0001`
- ^ What does this do?


## Create Models 


## Create Views


## Create Templates