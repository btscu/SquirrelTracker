from . import views
from django.urls import path

urlpatterns = [
        path('', views.homepage),
       # path('sightings', views.all_sights),
       # path('sightings/add/', views.add_sights),
       # path('sightings/stats/', views.stats),
       # path('sightings/<Unique_Squirrel_Id>/', views.find_squirrel)
       # path('map/', views.map)
]
