from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path
# from . import data
from django.template import loader
from bs4 import BeautifulSoup
import requests

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
        chargespot["lat"] = tag.select_one('lat').text
        chargespot["lng"] = tag.select_one('lng').text
        chargespot_list.append(chargespot)


    return render(request, 'map/main.html', {"chargespot_list": chargespot_list})

def map(request):
    return render(request, 'map/map.html')

def map_data(request):
    url ='http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=s7Ytkl8dJDy32JsmhtlyMEGVjWPfEcBuXNnDCYQHitUBkHblPkhsXakF6aMhFf6NFOcxj6RFnuim5wTJUPNrkQ%3D%3D'
    res = requests.get(url)
    res.encoding = None
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(res.text)
    all = soup.select('item')
    chargespot_list = []
    for tag in all:
        if "종로구" in str(tag.select_one('addr').text):
            chargespot = {"statNm" : "" , "address" : "","lat" : "" , "lng" : "" }
            chargespot["statNm"] = str(tag.select_one('statNm').text)
            chargespot["address"] = str(tag.select_one('addr').text)
            chargespot["lat"] = str(tag.select_one('lat').text)
            chargespot["lng"] = str(tag.select_one('lng').text)
            chargespot_list.append(chargespot)

    # return render(request, 'map/map.html', {"chargespot_list_rat": chargespot_list[0]["rat"], "chargespot_list_lng": chargespot_list[0]["lng"]})
    return JsonResponse(chargespot_list, safe=False)
