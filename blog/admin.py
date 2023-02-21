from django.contrib import admin
from .models import Category,BlogPost

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)
