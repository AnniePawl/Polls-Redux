# View Layer

Views encapsulate the logic responsible for processing a user's request and returning response. Each view is responnsible for doing one of two things: returning an HttpResponse object, or raising an exception(e.g 404). <br>

## The Basics

- Web pages and other content are delivered with views
- Each view is depicted by a single function
- Each view responsible for two things: returning HttpResponse object or raising an error
- Django will choose a view by examining the URL that is requested
- All Django wants is an HTTPResponse

**View:** Master class-based view. All other views inherit from this <br>
**ListView:** A page representing list of objects<br>
**Detail View:** Contains object that view is operating upon<br>
**Template View:** Renders a given template, with context from URL<br>
**Class-based Views:** Code resusability (can be inherited by other views), DRY (reduced code duplication), Code Extendability (can include more funcionality like Mixins), Code structuring<br>
**Function-based Views:** Simple to implement, easy to read, explicit code flow, good for one-off of specialized functionality, harder to extend and reuse

## View Example:

**mysite/news/views.py**

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
```

## Mapping URLs to Views

To display a view at a specific URL, you need to create a **URLconf**. Add **namespaces** to URLconfs to help Django differenciate between URL names.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

When a user requests a page, Django will load **mysite.urls** and looks for the variable **url patterns**. Then it traverses the patterns in order and stops are first match. When it finds a match, Django imports and calls the given view. If there is no match, it will return an error.<br>

- You should **always use include() when you include other url patterns**
- `path() function` is passed four arguments, two required (route and view), and two optional(kwargs and naeme)
