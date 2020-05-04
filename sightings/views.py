from django.shortcuts import render
from django.http import HttpResponse
from .models import SquirrelViewing
from .modelform import ViewForm


# def index(request):
#    return HttpResponse('Squirrel Sightings')


def homepage(request):
    return render(request,'templates/home.html')


def squirrel_list(request):
    squirrels = SquirrelViewing.objects.all()
    info = ['Unique_Squirrel_Id', 'Longitude', 'Latitude', 'Date', 'Shift']
    context = {
            'squirrels':squirrels
            }

    return render(request, 'templates/list.html', context)




def specific_squirrel(request, Unique_Squirrel_Id):
    specific_squirrel  = SquirrelViewing.objects.get(unique_squirrel_id = Unique_Squirrel_Id)
    info = ['Unique_Squirrel_Id', 'Longitude', 'Latitude', 'Date', 'Shift', 'Age']
    form = ViewForm(instance = specific_squirrel)
    context = {
            'squirrels':specific_squirrel
            }
    return render(request, 'templates/specific_squirrel.html', context)


def squirrel_map(request):
    squirrels = SquirrelViewing.objects.all()[100:]
    context = {
            'squirrels':squirrels
            }
    return render(request, 'templates/squirrel_map.html', context)

# Create your views here.
