from django.shortcuts import render

# Create your views here.
def LoginPage(request):
    return render(request,'auth/login.html')

def RegisterPage(request):
    return render(request,'auth/register.html')

def studentLogin(request):
    return render(request,'auth/student-login.html')

def studentRegister(request):
    return render(request,'auth/student-register.html')


