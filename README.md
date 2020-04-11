## Django Poll App

Django is a python-based web framework that follows the **model-template-view** architechtual pattern. Django is fast, secure, and scalable! This is my first Django project, a simple poll app built with help from [this tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/). It consists of a public site that lets people view polls and vote in them, as well as an admin site to add, change, and delete polls.

### Getting Started

- Download this repo
- Make sure you have Django installed: `$ python -m django --version`
- Run development server `$ python manage.py runserver`

### Django Basic Overview

For more detailed notes, take a look at the [notes folder](https://github.com/AnniePawl/Django-Poll-App/tree/master/django_notes) in this repo.<br><br>

**Models** <br>
[My models notes](https://github.com/AnniePawl/Django-Poll-App/blob/master/django_notes/Models.md) <br>
A model is a single, definitive source of truth that contains essential feilds and behaviors for data. You can use Django w/o a database, but it comes with an object-relational mapper. When models are defined, Django can automatically creates a professional adnminstrative interface. <br><br>

**Templates** <br>
[My template notes](https://github.com/AnniePawl/Django-Poll-App/blob/master/django_notes/Templates.md) <br>
Templates define the look and feel of a site and provides "holes" for child templates to fill. <br><br>

**Views**<br>
[My view notes](https://github.com/AnniePawl/Django-Poll-App/blob/master/django_notes/Views.md) <br>
A view is a type of webpage that generally serves a specific function and has a specific template. Each view is responsible for doing one of two things: returning an HttpResponse object, or raising an exception. <br><br>

### Basic steps to create an app

- Check out my [cheet sheet](https://github.com/AnniePawl/Django-Poll-App/blob/master/django_notes/Cheat_Sheet.md)
- Check out basic [django file structure](https://github.com/AnniePawl/Django-Poll-App/blob/master/django_notes/Django_Structure.md)

### Resources

For more detailed information, check out the [Django Documentation](https://docs.djangoproject.com/en/3.0/)
