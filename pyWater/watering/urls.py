from django.forms import forms
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'watering'

urlpatterns = [
    path('addplant',views.add_plant,name='add_plant'),
    path('plants',views.show_plants,name='plants_list'),
    path('watering',views.water,name='watering'),
    path('<int:name>/',views.show_water,name='water')
]

