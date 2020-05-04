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

def stats(request):
    squirrels = SquirrelViewing.objects.all()
    overall_total = SquirrelViewing.objects.all().count()
    number_AM = squirrels.filter(shift='AM').count()
    number_PM = squirrels.filter(shift = 'PM').count()
    percent_AM = number_AM/squirrels.count()
    percent_PM = number_PM/squirrels.count()
    number_Adult = squirrels.filter(age = 'Adult').count()
    number_Juvenile = squirrels.filter(age = 'Juvenile').count()
    number_Unknown = squirrels.filter(age = '').count()
    total_n = number_Adult + number_Juvenile + number_Unknown
    percent_Adult = number_Adult/total_n
    percent_Juvenile = number_Juvenile/total_n
    percent_Unknown = number_Unknown/total_n

    context = {
            'Total':overall_total,
            'Morning':number_AM,
            'Night':number_PM,
            'Morning_Percent':percent_AM,
            'Night_Percent':percent_PM,
            'Adult_Number':number_Adult,
            'Juvenile_Number':number_Juvenile,
            'Number_Unknown':number_Unknown,
            'Adult_Percent':percent_Adult,
            'Juvenile_Percent':percent_Juvenile,
            'Unknown_Percent':percent_Unknown
            }
    return render(request, 'templates/squirrel_stats.html', {'context':context})




# Create your views here.
