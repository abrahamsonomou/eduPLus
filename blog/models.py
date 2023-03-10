from django.db import models
import uuid
from django.urls import reverse
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field
from accounts.models import User
from core.models import Category


# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class BlogPost(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique=True) #Unique identifier for the article
    title = models.CharField(max_length=200, unique=True) #Title of the Article
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True, related_name='blog_posts') #Author of the Article
    description = models.TextField(blank=True,null=True) #Short Description of the article
    content = CKEditor5Field(config_name='extends') #Content of the article, you need to install CKEditor
    category = models.ForeignKey(Category, related_name='category_blog', on_delete=models.CASCADE) #Category of the article
    tags = TaggableManager() #Tags for a Particular Article, You need to install Taggit
    views = models.IntegerField(default=0)
    is_popular = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog/images') #Cover Image of the article
    bg = models.ImageField(upload_to='blog/bg_images', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True) #Date of creation
    updated_on = models.DateTimeField(auto_now=True) #Date of updation
    status = models.IntegerField(choices=STATUS, default=0) #Status of the Article either Draft or Published
    active=models.BooleanField(default=True,verbose_name="status")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.pk})




