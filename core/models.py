from django.db import models
import uuid
from django.urls import reverse
# from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field
from accounts.models import User
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Category(TranslatableModel):
    translations = TranslatedFields(
    category_name=models.CharField(max_length=200,verbose_name="Category Name"),
    description=models.TextField(blank=True,null=True,verbose_name="Description"),
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date'),
    )
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    image=models.ImageField(upload_to='cours/Category',blank=True,null=True)
    active=models.BooleanField(default=True,verbose_name="status")
#
# class Category(models.Model):
#     uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     category_name=models.CharField(max_length=200,verbose_name="Category Name")
#     description=models.TextField(blank=True,null=True,verbose_name="Description")
#     created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
#     updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
#     active=models.BooleanField(default=True,verbose_name="status")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    
    def __str__(self) -> str:
        return self.category_name
        
class SubCategory(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,
                               blank=True,
                               null=True,related_name="fk_category",
                               verbose_name="Category")
    image=models.ImageField(upload_to='cours/SubCategory',blank=True,null=True)
    sub_category_name=models.CharField(max_length=200,verbose_name="Category Name")
    description=models.TextField(blank=True,null=True,verbose_name="Description")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    active=models.BooleanField(default=True,verbose_name="status")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categorys'
    
    def __str__(self) -> str:
        return self.category_name
    
