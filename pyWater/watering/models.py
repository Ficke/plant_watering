from django.db import models

class Plant(models.Model):
    plant_name = models.CharField(max_length=200)
    plant_type = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added')
    def __str__(self):
        return self.plant_name


class Watering(models.Model):
    watered_plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    water_date = models.DateTimeField('date watered')
    def __str__(self):
        return self.watered_plant.plant_name

