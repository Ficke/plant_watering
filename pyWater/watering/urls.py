from django.forms import forms
from django.urls import path

from . import views

app_name = 'watering'

urlpatterns = [
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<str:plant_name>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # #path('<str:plant_name>/results/', views.results, name='results'),
    # #ex: /watering/Thanksgiving%20Cactus/
    # path('<str:plant_name>/water/', views.water, name='water'),
    # #ex: /watering/form
    path('plant_form',views.add_plant,name='add plant'),
    path('plants',views.show_plants,name='plants list'),
    path('watering',views.water,name='watering'),
]

