## Django Admin

Once models are defined, Django can automatically generate a professional admin interface. Authenticated users can add, change, and delete objects.

### Creating Admin user

1. Run command `$python3 manage.py createsuperuser`
2. Answer the prompts (username, password)
3. Start development server `$python3 manage.py runserver`
4. Go to local host/admin
5. Make updates and save

### Register model in admin site

Edit the admin.py file to tell Admin that spcific objects have an admin interface <br>

**mysite/news/models.py**

```python
from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
```

**mysite/news/admin.py**

```python
from django.contrib import admin

from . import models

admin.site.register(models.Article)
```
