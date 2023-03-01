from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from contact.forms import ContactForm
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'client/pages/home.html')

def about(request):
    return render(request,'client/pages/about.html')

@csrf_exempt
def contact(request):
    form=ContactForm(request.POST)
    if request.method=='POST':
        nom=request.POST.get('nom')
        email=request.POST.get('email')
        message=request.POST.get('message')

        print(nom,email,message)
        if form.is_valid():   
            instance=form.save(commit=False)
            instance.save()

            # from_email = settings.ADMIN_EMAIL
            
            # f=f'''E-mail de Contact de EDUPLUS

            # Nom du client : {nom}
            # E-mail du client : {email}
            # Méssage : 
            #     {message}
            # '''


            # send_mail(
            # 'VOUS AVEZ ÉTÉ CONTACTÉ DEPUIS EDUPLUS',
            # # message,
            # f,
            # from_email,
            # [email],
            # fail_silently=False,
            # )

            return redirect("/")

    context={
    'form':form,
    }  
    return render(request,'client/pages/contact.html',context)

def blog(request):
    return render(request,'client/pages/blog.html')

def blogDetails(request):
    return render(request,'client/pages/blog-detail.html')

def shop(request):
    return render(request,'client/pages/shop.html')

def shopProductDetail(request):
    return render(request,'client/pages/shop-product-detail.html')

def checkout(request):
    return render(request,'client/pages/checkout.html')

def cart(request):
    return render(request,'client/pages/cart.html')


def instructors(request):
    return render(request,'client/pages/instructors.html')

def instructorDetails(request):
    return render(request,'client/pages/instructorDetails.html')

def becomeInstructor(request):
    return render(request,'client/pages/become-instructor.html')



def coursDetails(request):
    return render(request,'client/pages/coursDetails.html')

def coursCategorie(request):
    return render(request,'client/pages/coursCategorie.html')

def cours(request):
    return render(request,'client/pages/cours.html')  

def examen(request):
    return render(request,'client/examen/examen.html')  