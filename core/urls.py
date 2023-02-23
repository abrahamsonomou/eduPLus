from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/',include('accounts.urls')),
    path('about', views.about, name='about'),

    path('shop', views.shop, name='shop'),
    path('shopProductDetail', views.shopProductDetail, name='shopProductDetail'),


    path('cours', views.cours, name='cours'),
    path('coursCategorie', views.coursCategorie, name='coursCategorie'),
    path('coursDetails', views.coursDetails, name='coursDetails'),

    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),

    path('instructors', views.instructors, name='instructors'),
    path('instructorDetails', views.instructorDetails, name='instructorDetails'),
    path('becomeInstructor', views.becomeInstructor, name='becomeInstructor'),

]

