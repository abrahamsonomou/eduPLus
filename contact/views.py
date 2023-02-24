from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import  generics
from rest_framework.permissions import IsAdminUser
from django.views.generic.edit import CreateView
from .forms import *
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
    
# Create your views here.
def contact_success(request):
    return render(request,'contact/contact_success.html')

class Contacts(CreateView):
    model=Contact
    form_class=ContactForm
    template_name='contact/contact.html'
    success_url='contact_success'

def contact(request):
    form=ContactForm(request.POST)
    if form.is_valid():   
        instance=form.save(commit=False)
        instance.save()
        nom=form.cleaned_data['nom']
        email=form.cleaned_data['email']
        sujet=form.cleaned_data['sujet']
        message=form.cleaned_data['message']
        html_ =message
        txt_ ="test.txt"
        from_email = settings.DEFAULT_FROM_EMAIL
        
        recipient_list = [email]
        
        sent_mail = send_mail(
        sujet,
        txt_,
        from_email,
        recipient_list,
        html_message=html_,
        fail_silently=False,
        )
        
    context={
    'form':form,
    }
        
    return render(request,"contact/contact.html",context)
    
class ContactList(generics.ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    permission_classes = [IsAdminUser]
    
class ContactListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer    
    permission_classes = [IsAdminUser]
    