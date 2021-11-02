from django.contrib import admin
from .models import Watering, Plant

class WateringInline(admin.StackedInline):
    model = Watering
    extra = 3

class PlantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['plant_name']}),
        ('Date information', {'fields': ['added_date']}),
    ]
    inlines = [WateringInline]

admin.site.register(Plant, PlantAdmin)
