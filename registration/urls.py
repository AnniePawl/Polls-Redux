from django.urls import path
from . import views

app_name = 'registration:signup'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

]
