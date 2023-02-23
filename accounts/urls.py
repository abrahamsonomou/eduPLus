from django.urls import path

from . import views

urlpatterns = [
    path('login', views.LoginPage, name='login'),
    path('register', views.RegisterPage, name='register'),

    path('studentLogin', views.studentLogin, name='studentLogin'),
    path('studentRegister', views.studentRegister, name='studentRegister'),

    
]

