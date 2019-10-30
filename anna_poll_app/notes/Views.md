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
- ```    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail')
    ```
  

**Example**
If someone types URL `/polls/34 -> <br>
Django will load **mysite.urls**. Finds varaible named **url patterns** and traverses the patterns in order/ 
- Finds match at `polls/`, strips off matching text "polls/" and returns remaining text ("34") to polls.urls URL conf for further processing 


## URL Pattern 
**/newsarchive/<year>/<month>/**
**Blog App Views Example**
- *Blog Homepage* - displays latest few entries 
- *Comment Action*- handles posting comments to a given entry
- *Question Index Page* - Displays latest few questions
- *Question Detail Page*- Displays question text 
- *Day-Based Archive*- Displays all page entires on given day