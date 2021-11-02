from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Watering, Plant
from django.forms import ModelForm
from watering.models import Plant
from .forms import PlantForm, WateringForm

# #Watering page: this is an input for when you water the plant
def water_plant(request):
    return HttpResponse("You're watering the Plant.")

#add plant page: this is the page where you add more plants
#this should return to the index when you're done adding the plants 

#test form


def confirm(request):
    return HttpResponse("You just submitted a plant name")


#this will display the last 5 plants you've added
def show_plants(request):
    latest_plants = Plant.objects.order_by('-added_date')[:5]
    output = ', '.join([n.plant_name for n in latest_plants])
    return HttpResponse(output)

def add_plant(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlantForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
        return HttpResponseRedirect('/watering/plants')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlantForm()

    return render(request, 'watering/name.html', {'form': form})

def water(request):
    if request.method == 'POST':
        form = WateringForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/watering/plants')
    else: 
        form = WateringForm()
        
    return render(request,'watering/name.html',{'form':form})




        










