from django.contrib import admin
from .models import Category,SubCategory
from import_export.admin import ImportExportModelAdmin
from parler.admin import TranslatableAdmin

# Register your models here.
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['category_name','active',]
admin.site.register(Category,TranslatableAdmin)
# admin.site.register(Category,CategoryAdmin)

class SubCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['sub_category_name','category','active',]
admin.site.register(SubCategory,SubCategoryAdmin)

