from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def LoginPage(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email,password)
    # user = authenticate(email=email, password=password)
    user = authenticate(username=email, password=password)

    if user is not None and user.is_active:
        login(request, user)
        return redirect('/')

    return render(request,'auth/login.html')

def LogoutPage(request):
    logout(request)
    return render(request,'auth/login.html')

def RegisterPage(request):
    return render(request,'auth/register.html')

def studentLogin(request):
    return render(request,'auth/student-login.html')

def studentRegister(request):
    return render(request,'auth/student-register.html')


