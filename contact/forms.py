from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['nom','email','message']
        labels={'nom':'Full Name','email':'Email Address','message':'Message'}
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':"Abraham SONOMOU",'required':'required',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':"test@gmail.com",'required':'required',}),
            'message':forms.Textarea(attrs={'class':'form-control','cols':30,'rows':10,'required':'required',})
        }
        
        