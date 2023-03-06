from django.urls import path
from .views import *

urlpatterns = [
    path(r'',index,name="quiz"),
    path(r'get_quiz',get_quiz,name="get_quiz"),
]
