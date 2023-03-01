from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
#   email = request.POST.get('email')
#     password = request.POST.get('password')
#     print(email,password)
#     # user = authenticate(email=email, password=password)
#     user = authenticate(username=email, password=password)

#     if user is not None and user.is_active:
#         login(request, user)
#         return redirect('/')

#     return render(request,'auth/login.html')

def LoginPage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    if request.method== "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            
            #user=authenticate(email=email,password=password)
            user=User.objects.filter(email=email).first()
            if user and check_password(password, user.password):
                print(user)
                if user is not None:
                    #users=User.objects.filter(email=email).first()
                    if not user.is_active:
                        messages.error(request,"Votre compte n'est pas activé, veuillez contacter l'administrateur")
                        return render(request,"auth/login.html",{"form":form})
                    
                    login(request,user)
                    return redirect('home')
            else:
                messages.error(request,"Autehtification echouee. Vos informations sont incorrectes")
                return render(request,"auth/login.html",{"form":form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+= ' is-invalid'
            return render(request,"auth/login.html",{"form":form})
    else:
        form=LoginForm()
    return render(request,"auth/login.html",{"form":form})


def LogoutPage(request):
    logout(request)
    return redirect('home')

def RegisterPage(request):
    if request.method== "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            password_confirm=form.cleaned_data['password_confirm']
            
            if password != password_confirm:
                messages.error(request,'Mot de passe non identique')
                return render(request,'auth/register.html',{'form':form})
            else:
                user=User.objects.filter(email=email).first()
                if user is not None:
                    messages.error(request,'Cet email existe')
                    return render(request,'auth/register.html',{'form':form})
                else:
                    user=User.objects.create_user(email=email,password=password)
                    if user is not None:
                        login(request,user)
                        return redirect('login')
                    else:
                        messages.error(request,'Creation de compte echouee')
                        return render(request,'auth/register.html',{'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+= ' is-invalid'
            return render(request,"accounts/auth/register.html",{"form":form})
    else:
        form=RegisterForm(request.POST)
    return render(request,"accounts/auth/register.html",{"form":form})


def reset_password(request):
    return render(request,'auth/reset_password.html')

def studentLogin(request):
    return render(request,'auth/student-login.html')

def studentRegister(request):
    return render(request,'auth/student-register.html')


