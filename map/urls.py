from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name="add"),
    path('add2/', views.add2, name="add2"),
    path('map/', views.map, name="map"),
    path('mapdata/', views.map_data, name="map_data"),
    path('index/', views.index, name="index"),
    path('test/', views.test, name="test"),
]
