# Models

A model is a single, definitive source of information about you data. It contains essential fields and behvaiors of data. <br>
**The Basics**

- Every model is a python class that subclasses `django.db.models.Model`
- Each model attribute represents a database field
- Django automatically generates database-access API

## Model Example

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

^ This model would create the following database table:

```python
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

## Making Model Changes (3 Steps)

1. Change models in `models.py`
2. Change installed_apps setting to add name of module that contains your model.py

```python
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```

3. Run `$python3 manage.py makemigrations` to create migrations for those changes. Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc) into database scheme.
4. Run`$python3 manage.py migrate` to apply changes to databse

### Fields

Most important part of a model is **list of database fields it defines**.

- Each field should be instance of appropriate **field class**. This represents a database table column.
- Some field classes have required arguments, or optional requirements
- By default, Django gives each model the following field:
  `id = models.AutoField(primary_key=True)`

### Relationships

Relational databases are powerful. There are 3 common database relationships: <br>
**Many-to-one:** Manufacturer makes many cars, but each car has one manufacturer<br>
**Many-to-many:** Pizza has multiple topppings, and toppings can be on multiple pizzas<br>
**One-to-many:** Usually used when object "extends" another object in some way.
