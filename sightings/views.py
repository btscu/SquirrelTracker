from django.shortcuts import render
from django.http import HttpResponse
from .models import SquirrelViewing
from .modelform import ViewForm


# def index(request):
#    return HttpResponse('Squirrel Sightings')


def homepage(request):
    return render(request,'templates/home.html')



# Create your views here.
