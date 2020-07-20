from django.shortcuts import render
from django.urls import path
# from . import data
from django.template import loader

def main(request):
    return render(request, 'map/main.html', {})

def map(request):
    return render(request, 'map/map.html', {})
