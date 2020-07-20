from django.shortcuts import render
from django.urls import path
# from . import data
from django.template import loader
from bs4 import BeautifulSoup
import requests
import json



def main(request):
    url ='http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=s7Ytkl8dJDy32JsmhtlyMEGVjWPfEcBuXNnDCYQHitUBkHblPkhsXakF6aMhFf6NFOcxj6RFnuim5wTJUPNrkQ%3D%3D'
    res = requests.get(url)
    res.encoding = None
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(res.text)
    all = soup.select('item')
    chargespot_list = []
    for tag in all:
        chargespot = {"lat" : "" , "lng" : "" }
        chargespot["lat"] = str(tag.select_one('lat').text)
        chargespot["lng"] = str(tag.select_one('lng').text)
        chargespot_list.append(chargespot)
    return render(request, 'map/main.html', {"chargespot_list": chargespot_list})

def map(request):
    url ='http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=s7Ytkl8dJDy32JsmhtlyMEGVjWPfEcBuXNnDCYQHitUBkHblPkhsXakF6aMhFf6NFOcxj6RFnuim5wTJUPNrkQ%3D%3D'
    res = requests.get(url)
    res.encoding = None
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(res.text)
    all = soup.select('item')
    chargespot_list = []
    for tag in all:
        chargespot = {"lat" : "" , "lng" : "" }
        chargespot["lat"] = str(tag.select_one('lat').text)
        chargespot["lng"] = str(tag.select_one('lng').text)
        chargespot_list.append(chargespot)
    return render(request, 'map/map.html', {"chargespot_list": chargespot_list} )


