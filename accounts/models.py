from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import BaseUserManager
import uuid
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,password=None,*callback_args, **callback_kwargs):
        
        if not email:
            raise ValueError('Desolé, veuillez saisir un email')
        
        email=self.normalize_email(email)
        user=self.model(email=email)
        
        user.set_password(password)
        
        # user=self.model(username=username,password=password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        
        user.save(using=self._db)
        return user   

class Profession(models.Model):   
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(verbose_name='Title',max_length=200)
    description=models.TextField(null=True,blank=True,)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name="Profession"

    def __str__(self) -> str:
        return self.title

class Specialite(models.Model):   
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(verbose_name='Title',max_length=200)
    description=models.TextField(null=True,blank=True,)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name="Specialite"

    def __str__(self) -> str:
        return self.title
        
class User(AbstractUser):
	uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)

	email = models.EmailField(db_index=True, unique=True)
	username = None 
	last_name = models.CharField(max_length=250, blank=True, null=True)
	first_name = models.CharField(max_length=250, blank=True, null=True)
	midle_name = models.CharField(max_length=250, blank=True, null=True)
	photo = models.ImageField(upload_to='users/photos/',blank=True, null=True)
	about = models.TextField(blank=True, null=True)

	twitter = models.CharField(
	    blank=True, null=True, name='twitter', verbose_name="Twitter", max_length=200)
	facebook = models.CharField(
	    blank=True, null=True, name='facebook', verbose_name="Facebook", max_length=200)
	instagram = models.CharField(
	    blank=True, null=True, name='instagram', verbose_name="Instagram", max_length=200)
	linkdin = models.CharField(
	    blank=True, null=True, name='linkdin', verbose_name="Linkdin", max_length=200)
	youtube = models.CharField(
	    blank=True, null=True, name='youtube', verbose_name="Linkdin", max_length=200)

	telephone= PhoneNumberField(null=False, blank=False)
	profession=models.ForeignKey(Profession,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_profession")
	specialite=models.ForeignKey(Specialite,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_specialite")
	pays = CountryField(null=True,blank=True,blank_label='(select country)')
	
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	# A timestamp representing when this object was created.
	created_at = models.DateTimeField(auto_now_add=True)

	# A timestamp reprensenting when this object was last updated.
	updated_at = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	def __str__(self):
		if self.is_student:
				type_ = 'Student'
		elif self.is_teacher:
			type_ = 'Teacher'
		else:
			type_ = 'None'
		return f'{type_}: {self.email}'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.photo:
			pic = Image.open(self.photo.path)
			if pic.width > 256:
				pic.thumbnail((256, pic.height / (pic.width / 265)))
				pic.save(self.photo.path)


	def get_photo_url(self):
		if self.photo:
			return self.photo.url
		else:
			if self.is_student:
				return '/media/users/students/student-default.png'
			elif self.is_teacher:
				return '/media/users/teachers/teacher-default.png'
			else:
				return '/media/users/default.png'

	def get_photo_name(self):
		if self.photo:
			return self.photo.name 
		else:
			if self.is_student:
				return 'student-default.png'
			elif self.is_teacher:
				return 'teacher-default.png'
			else:
				return 'default.png'

	def get_profile(self):
		if self.is_student:
			return Student.objects.get(user=self)
		elif self.is_teacher:
			return Teacher.objects.get(user=self)
		else:
			return None

	def get_shortname(self):
		return f'{self.first_name[0:1]}.{self.last_name}'

	def get_fullname(self):
		return f'{self.first_name} {self.last_name}'
		
	objects= UserProfileManager()

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
	interested_category=models.TextField(blank=True,null=True,verbose_name="Interested category")
	
	def __str__(self) -> str:
		return f'{self.user.email}'

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
	
	def __str__(self) -> str:
		return f'{self.user.email}'
	
# la class Competence
VALEURS = (
    (0, "50"),
    (1, "60"),
    (2, "80"),
    (3, "90"),
)

class Competence(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(verbose_name='Title',max_length=200)
    pourcentage=models.IntegerField(choices=VALEURS, default=0,null=True,blank=True,verbose_name="Pourcentage")
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Teacher',related_name="fk_teacher_competence")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name="Competences"

    def __str__(self) -> str:
        return self.title
