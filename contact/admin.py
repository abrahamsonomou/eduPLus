from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('nom','email','message','updated')

admin.site.register(Contact,ContactAdmin)


class NewsLetterAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('email','created',)

admin.site.register(NewsLetter,NewsLetterAdmin)

    