from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Register your models here.
class UserForm(forms.ModelForm):
    class Meta:
        widgets = {
            'telephone': PhoneNumberPrefixWidget(initial='GN'),
        }


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =( 'email','specialite','is_student','is_teacher', 'is_active', 'is_staff', 'created_at', 'updated_at') 
    ordering=('updated_at',)  
    form = UserForm

@admin.register(Profession)
class ProfessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('title','description',)

@admin.register(Specialite)
class SpecialiteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('title','description',)

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('user','interested_category',)

class CompetenceAdmin(admin.StackedInline):
    model= Competence

class TeacherAdmin(admin.ModelAdmin):
    inlines=[CompetenceAdmin]

admin.site.register(Teacher,TeacherAdmin)

@admin.register(Competence)
class CompetenceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('title','pourcentage','teacher','updated')
