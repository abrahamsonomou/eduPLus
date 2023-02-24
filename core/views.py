from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.utils.translation import gettext as _

# Create your views here.
def home(request):
    return render(request,'client/pages/home.html')

def about(request):
    return render(request,'client/pages/about.html')

def contact(request):
    form=ContactForm(request.POST)
    if form.is_valid():   
        instance=form.save(commit=False)
        instance.save()

        
        nom=form.cleaned_data['nom']
        email=form.cleaned_data['email']
        message=form.cleaned_data['message']

        # from_email = settings.DEFAULT_FROM_EMAIL
        
        email = EmailMessage(
        _('Nouveau message de myealearning'),
        content,
        _('myealearning'),
        [config('ADMIN_EMAIL')],
        headers = { 'Reply-To': contact_email }
        )
        email.send()
        messages.success(request, _('Thank you ! We will check in as soon as possible ;-)'))
            
        return redirect("home")
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