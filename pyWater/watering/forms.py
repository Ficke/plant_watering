from django import forms
from django.forms import ModelForm 
from .models import Plant, Watering


#this is the form that adds a plant 
#it takes

class WateringForm(ModelForm): 
    class Meta: 
        model = Watering
        fields = "__all__"

#Form to add plants 
class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
        #help_texts = {'plant_name': ('Enter the name of your plant'),
        #'plant_type': ('Enter the type of plant'),
        #'added_date': ('Enter when you obtained the plant')}



