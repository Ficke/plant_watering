from django.conf.urls import url
from django.urls.conf import path
from . import views
from django.contrib.auth import login


urlpatterns = [
    path('',views.home), 
]
