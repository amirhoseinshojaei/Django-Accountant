from .import views
from django import urls
from django.urls import path
# wirte code here
urlpatterns=[
    path('signup/',views.register, name= 'register'),
    path ('login/', views.login , name= 'login'),
    path ('reset/token/', views.reset_token , name= 'reset_token'),

]