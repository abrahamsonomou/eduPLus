from django.db import models
import uuid

# Create your models here.
# Contact
class Contact(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        ordering=['-updated']
        verbose_name="Contact" 

    def __str__(self) -> str:
        return self.nom

class NewsLetter(models.Model):
    email=models.EmailField(blank=True,null=True,max_length=100,verbose_name='Email',name='email')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    
    class Meta:
        verbose_name="NewsLetter"
        ordering=['-created']

    def __str__(self) -> str:
        return self.email
        