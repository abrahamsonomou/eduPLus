from django import forms
from django.forms.widgets import TextInput

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control border-0 bg-light rounded-end ps-1',"placeholder":"E-mail"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border-0 bg-light rounded-end ps-1', "placeholder":"*********"}))

class RegisterForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control border-0 bg-light rounded-end ps-1',"placeholder":"E-mail"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border-0 bg-light rounded-end ps-1','placeholder':'*********'}))
    password_confirm=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border-0 bg-light rounded-end ps-1', "placeholder":"*********"}))