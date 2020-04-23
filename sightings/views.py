from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Squirrel Sightings')

# Create your views here.
