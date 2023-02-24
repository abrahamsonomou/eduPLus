from django.urls import path
from .views import *

urlpatterns = [
    path('',Contacts.as_view(),name='contact'),
    # path('',contact,name='contact'),
    path('contact_success',contact_success,name='contact_success'),
    
    path(r'api/Contacts/',ContactList.as_view(),name='Contacts/'),
    path(r'api/(?P<pk>[0-9]+)/$', ContactListDetail.as_view(),name='Contactdetails/'),
]
