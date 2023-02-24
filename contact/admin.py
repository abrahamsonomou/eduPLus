from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','message','updated')

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display=('email','created',)

    