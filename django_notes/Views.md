# Views

A view is a "type" of web page that generally servers a specific function and has a specific template. <br>

- Web pages and other content are delivered with views
- Each view is depicted by a single function
- Each view responsible for two things:
  - Returning HttpResponse Object containing content of requested page
  - Raising a exception like Http404
- Django will choose a view by examining the URL that's requested
- All Django wants is n **HTTPResponse**

## Process

1. Add new view to `view.py`

- ```def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
  ```

2. Wire new view into `poll.urls` module by adding path calls

- ```# ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail')
  ```

### Example

If someone types URL `/polls/34 -> <br>
Django will load **mysite.urls**. Finds varaible named **url patterns** and traverses the patterns in order.

- Finds match at `polls/`, strips off matching text "polls/" and returns remaining text ("34") to polls.urls URL conf for further processing

```from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
```

## URL Pattern

**/newsarchive/<year>/<month>/**
**Blog App Views Example**

- _Blog Homepage_ - displays latest few entries
- _Comment Action_- handles posting comments to a given entry
- _Question Index Page_ - Displays latest few questions
- _Question Detail Page_- Displays question text
- _Day-Based Archive_- Displays all page entires on given day

## Class-Based View

**Pros**

- Code resusability (can be inherited by other views)
- DRY, reduced code duplication
- Code Extendability, can include more funcionality like Mixins
- Code structuring
- Built in genertic class-based views

## Function Based View

**Pros**

- simple to implement
- easy to read
- explicit code flow
- good for one-off of specialized functionality
  **Cons**
- Hard to extend and resuse
- Handling of HTTP methods

### View

Master class-based view. All other views inherit from this

## ListView

A page representing list of objects

## Detail View

Contains object that view is operating upon

## Template View

Renders a given template, with context from URL
