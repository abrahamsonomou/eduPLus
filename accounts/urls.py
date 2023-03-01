from django.urls import path

from . import views

urlpatterns = [
    path('login', views.LoginPage, name='login'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('register', views.RegisterPage, name='register'),
    path('logout', views.LogoutPage, name='logout'),

    path('studentLogin', views.studentLogin, name='studentLogin'),
    path('studentRegister', views.studentRegister, name='studentRegister'),

    
]

