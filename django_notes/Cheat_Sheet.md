
1. Check version of Django 
- `$ python -m django --version` 

2. Auto generate code to establish Django project 
- `$ django-admin startproject mysite` 

3. Put code somewhere outside document root like, home/mycode


5. Create apps within project
-  Make sure you are in same directory as manage.py
- `$python3 manage.py startapp appName`

6. Write your first **VIEW!** <br/>
`appName/views.py`. To call a view, next you must map it to a URL with a **URLconf** <br/>
Each time you create a new view, wire them into the **polls.url** by adding the right path() calls. 

``` from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

7. Create a **URLconf** in app directory. <br/>`appName/urls.py` <br/>
``` from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

8. Point **root URLconf** in mysite/urls.py. 
The include function allows referencing other URL confs. When Django encounters `include()`, it chops of part of URL matched to that point and sents remaining string to the include() URLconf for further processing. 
- You should **always use include() when you include other url patterns**
- `path() function` is passed four arguments, two required (route and view), and two optional(kwargs and naeme)

```from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

4. Start Django development server, lightweight web server 
- Development servere auto reloads code for each request as needed
- `$ python manage.py runserver`

6. Creates tables in database
- `$python manage.py migrate`

7. Include app in project by refererncing config class in INSTALLED_APP setting 
- `$python3 manage.py makemigrations polls`

8. Create an Admin User
- `$python3 manage.py createsuperuser`
- Enter desired username, email address, and password

- `python manage.py check` checks for any problems in project without making migrations or touching db

- `$ python manage.py sqlmigrate polls 0001`
- ^ What does this do?


### Create your first **Template**
    - Create a templates directory in 

## Create Views


## Create Templates