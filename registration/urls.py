from .import views
from django import urls
from django.urls import path
# wirte code here
urlpatterns=[
    path('signup/',views.register, name= 'signup'),
]