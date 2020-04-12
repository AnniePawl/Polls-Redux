1. `$ python -m django --version`. Make sure Django is installed and check version.

2. `$ django-admin startproject mysite`. Auto generates code to establish Django project. This creates a **my site** directory with this basic file structure:

```python
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

3. `$ python manage.py runserver`. Start Django development server, which should auto reload code for each request as needed, to make sure you are in business.

4. `$ python manage.py startapp appName`. Create your first app! Make sure you are in same directory as manage.py. Remember that a single project can have multiple apps.

5. **appName/views.py**. Write your first view!

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

6. **appName/urls.py**. Map view to a URL. Each time you create a new view, wire it into the appName.urls.py by adding the right path() calls. Make sure to point to root _URLconf_.The include function allows referencing other URL confs. When Django encounters `include()`, it chops of part of URL matched to that point and sents remaining string to the include() URLconf for further processing. `path() function` is passed four arguments, two required (route and view), and two optional(kwargs and naeme)

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

7. **projectName/settings.py**. Make database changes here if necessary.

8. `$python manage.py migrate`. Creates any necessary database tables according to database settings by referencing INSTALLED_APPS

9. **appName/models.py**. Create your first model, which contains essential fields and behaviors of data you're storing.

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

```

10. **Activate models:** To include an app in project, we need to reference its configuration class in INSTALLED_APPS

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

11. `python manage.py makemigrations appName`. Tell Django you have made changes to models and you want them to be stored as a migration.

12. `$python3 manage.py createsuperuser`. Create an Admin User! Follow Prompts (username, email, password)

13. `$ python manage.py runserver`, then **localHost/admin** to see admin login

14. **appName/admin.py**. Make app modifiable in admin.

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)

```

15. Change, add, and delete questions/answers/ in admin interface

16. **appName/templates/appName/templateName.html**. Create templates to describe the look and feel of your app.

```html
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}
```

16. `$ python manage.py test appName` Create and run tests

17. `$ python manage.py check`. Checks for any problems in project without making migrations or touching db

18. **appName/static/appName/style.css** Create a static folder and customize how your app looks in a stylesheet.

19. Tell template to look for stylesheet:

```html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```
