from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('map/', views.map, name="map"),
    path('mapdata/', views.map_data, name="map_data"),
    path('index/', views.index, name="index")
]
