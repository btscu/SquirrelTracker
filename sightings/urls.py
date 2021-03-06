from . import views
from django.urls import path

urlpatterns = [
        path('', views.homepage),
        path('sightings/', views.squirrel_list),
        path('sightings/stats/', views.stats),
        path('sightings/<Unique_Squirrel_Id>/', views.specific_squirrel), 
        path('map/', views.squirrel_map)
]
