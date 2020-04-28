from django.urls import path
from . import views

# What is going wrong here?
# Which part needs to be 'registration:signup'


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
