from django.contrib import admin
from .models import BlogPost
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['title','author', 'category', 'tags', 'views', 'is_popular', 'created_on', 'updated_on', 'status',]

admin.site.register(BlogPost,BlogAdmin)
