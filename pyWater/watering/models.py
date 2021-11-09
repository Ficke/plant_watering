from django.db import models
from django.conf import settings
from django.urls import reverse

class Plant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Plant", null=True,editable=False)
    plant_name = models.CharField(max_length=200)
    added_date = models.DateField('date added')

    def __str__(self):
        return self.plant_name
    
    def get_absolute_url(self):
    #"""Returns the url to access a detail record for this book."""
        return reverse('plant-detail', args=[str(self.id)])


class Watering(models.Model):
    watered_plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    water_date = models.DateField('date watered')

    def __str__(self):
        return self.watered_plant.plant_name
    
    class Meta:
        ordering = ['water_date']

    



