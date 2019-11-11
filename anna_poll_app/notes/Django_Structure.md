## Django App Structure 

``` mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
``` 

### Outer `mysite/`
Root directory that contains project. Can be named anything 

### manage.py
A command-line utility that lets you interact with Django project in various ways 

### Inner `mysite/`
Actual python pacakge for project. Its name is python package name you'll need to use to import anythin inside it (e.g mysite.urls)

### mysite/__init__.py
An empty file that tell Python that this directory should be considerd a Python package. 

### mysite/settings.py
Settings/ configuration for Django project.

### mysite/urls.py
URL delcaratins. "Table of contents" of Django-powered site 

### mysite/wsgi.py 
An entry-point to WSGI-compatible web servers to serve project
