Point **root URLconf** in mysite/urls.py. 
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


### Namespacing 
Add namespaces to URLconfs to help Django differenciate between URL names