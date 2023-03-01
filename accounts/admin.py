from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =( 'email','is_student','is_teacher', 'is_active', 'is_staff', 'created_at', 'updated_at') 
    ordering=('email',)  

@admin.register(Profession)
class ProfessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('title','description',)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('user','interested_category',)


class CompetenceAdmin(admin.StackedInline):
    model= Competence

class TeacherAdmin(admin.ModelAdmin):
    inlines=[CompetenceAdmin]


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Competence)