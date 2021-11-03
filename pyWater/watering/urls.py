from django.forms import forms
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'watering'

urlpatterns = [
    url(r'^$',views.home),
    path('addplant',views.add_plant,name='add plant'),
    path('plants',views.show_plants,name='plants list'),
    path('watering',views.water,name='watering'),
    path('table',views.PlantView.as_view()),
]

