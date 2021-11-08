from django.contrib import admin
from .models import Watering, Plant

class WateringInline(admin.StackedInline):
    model = Watering
    extra = 3

class PlantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name information', {'fields': ['plant_name']}),
        ('Date information', {'fields': ['added_date']}),
    ]
    inlines = [WateringInline]

class WateringAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Plant Information', {'fields': ['watered_plant']}),
        ('Date information', {'fields': ['water_date']}),
    ]


admin.site.register(Plant, PlantAdmin)
admin.site.register(Watering, WateringAdmin)
