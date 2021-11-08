from django import forms
from django.forms import ModelForm 
from .models import Plant, Watering


#this is the form that adds a plant 
#it takes

class WateringForm(ModelForm): 
    
    class Meta: 
        model = Watering
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(WateringForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['watered_plant'].queryset = Plant.objects.filter(user=user)

    
#Form to add plants 
class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
        #help_texts = {'plant_name': ('Enter the name of your plant'),
        #'plant_type': ('Enter the type of plant'),
        #'added_date': ('Enter when you obtained the plant')}



