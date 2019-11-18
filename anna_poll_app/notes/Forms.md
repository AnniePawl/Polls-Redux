# Froms 
A form is a collection of elements inside a `<form></form>`that allow visitors to do things like enter text, select options, manipulate objects, etc... </br>

A form might include interface elements like checkboxes or drop downs. </br>

As well as `<input>`elemts, forms must also specidy two things:
1. **Where:** The URL to which data should be returned
2. **How:** The HTTP method the data should be returned by (GET or POST)

## GET and POST
**GET** and **POST** are the only HTTP methods to use when dealing with forms. </br>
**POST** used for anything that changes state of system</br>
**GET** used for requests that do not affect the state of the system. Get would be unsuitable for a password form because password would appear in URL and history of database! **security risk**

## Django and Forms 
Django handles three distinct parts of work involved in forms. Automates and simplifies. More secure
1. **preparing and restructuring data** to make it ready for rendering 
2. **Creating HTML forms** for the data
3. **Receiving and processing** submitted forms and data from the client. 

### Form Class
Everything starts w/ form class. Import forms module from Django. `from  django import forms`
```class FriendlyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
```

### Form Example
``` <form action='/submit' method='GET'>
Type your name here: <input type='text>


</form>
```