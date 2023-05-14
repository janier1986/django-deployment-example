from django.contrib import admin
from django.urls import path,include
from learning_templates import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from .views import *

app_name='learning_templates'

urlpatterns = [
    
    url(r'^relative_templates/$',views.url_templates,name='relative_templates'),
    url(r'^other/$',views.other,name='other'),

    
    
]