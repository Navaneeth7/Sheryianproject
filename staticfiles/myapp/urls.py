from django.urls import path
from .views import *
app_name='baseapp'
urlpatterns = [
    path('',home,name='home'),
    path('',courses,name='courses'),
    path('',bootcamp,name='bootcamp'),
    path('',requestcall,name='requestcall'),
    path('',home,name='home'),
    
]