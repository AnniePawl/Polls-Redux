# HTML Forms

A form is a collection of elements inside `<form></form>` that allows visitors to do things like enter text, select options, manipulate objects, etc... A form might include interface elements like checkboxes or drop downs. As well as `<input>`elements, forms must also specify two things:

1. **Where:** The URL to which data should be returned
2. **How:** The HTTP method the data should be returned by (GET or POST)

Django handles three distinct parts of work involved in forms.

1. **Preparing and restructuring data** to make it ready for rendering
2. **Creating HTML forms** for the data
3. **Receiving and processing** submitted forms and data from the client.

## Form Example

```html
<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %} {% for choice in question.choice_set.all %}
  <input
    type="radio"
    name="choice"
    id="choice{{ forloop.counter }}"
    value="{{ choice.id }}"
  />
  <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label
  ><br />
  {% endfor %}
  <input type="submit" value="Vote" />
</form>
```

### Building a Form in Django

Everything starts w/ form class. Firt, import forms module from Django. `from django import forms`

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

### The View Part

Don't forget that a view associated w/ form is needed. The data sent back to a Django site is processed by a view. To handle a form, we need to instantiate it in the view for the URL where we want it to be published.

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
```

### GET and POST

**GET** and **POST** are the only HTTP methods to use when dealing with forms. </br>
**POST** used for anything that changes state of system</br>
**GET** used for requests that do not affect the state of the system. Get would be unsuitable for a password form because password would appear in URL and history of database! **security risk**

### FormView vs. CreateView

**FormView:** Use when you need a form on a page and want to perform a certain action when valid form is submitted- like have a contact us form and sending an email on form submission. </br>
**CreateView:** Use when you want to insert a model instance in a database on form submission </br>
