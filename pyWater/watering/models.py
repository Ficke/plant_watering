from django.db import models
from django.conf import settings
from django.urls import reverse

class Plant(models.Model):
    plant_name = models.CharField(max_length=200)
    added_date = models.DateField('date added')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="Plant", 
        null=True,
        editable=False)

    def __str__(self):
        return self.plant_name
    
    def get_absolute_url(self):
        return reverse('watering:plants_list')


class Watering(models.Model):
    water_date = models.DateField('date watered')
    watered_plant = models.ForeignKey(
        Plant, 
        on_delete=models.CASCADE, 
        related_name='plants',
        related_query_name='watering',
)
    
    class Meta:
        ordering = ['water_date']

    def __str__(self):
        return self.watered_plant.plant_name
    
    def get_absolute_url(self): # new
        return reverse('watering:water', args=[str(self.id)])


    



