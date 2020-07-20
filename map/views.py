from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request,'map/index.html',{})

from bs4 import BeautifulSoup
import requests
url ='http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=s7Ytkl8dJDy32JsmhtlyMEGVjWPfEcBuXNnDCYQHitUBkHblPkhsXakF6aMhFf6NFOcxj6RFnuim5wTJUPNrkQ%3D%3D'
res = requests.get(url)
res.encoding = None
soup = BeautifulSoup(res.text, 'html.parser')
# print(res.text)
tags = soup.select('item')
chargespot_list = []
for tag in tags:
    chargespot = {"lat" : "" , "lng" : "" }
    chargespot["lat"] = tag.select_one('lat').text
    chargespot["lng"] = tag.select_one('lng').text
    chargespot_list.append(chargespot)

print(chargespot_list)