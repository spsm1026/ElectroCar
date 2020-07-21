from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path
# from . import data
from django.template import loader
from bs4 import BeautifulSoup
from .models import Sido, Goo

import requests

def map(request):
    sido_list = Sido.objects.order_by('sido_name')
    seoul = Sido.objects.get(id=1)
    goo_list = Goo.objects.filter(sido=seoul)

    return render(request, 'map/map.html', {"sido_list" : sido_list, 'goo_list': goo_list })

def map_data(request):
    url ='http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=s7Ytkl8dJDy32JsmhtlyMEGVjWPfEcBuXNnDCYQHitUBkHblPkhsXakF6aMhFf6NFOcxj6RFnuim5wTJUPNrkQ%3D%3D'
    res = requests.get(url)
    res.encoding = None
    soup = BeautifulSoup(res.text, 'html.parser')
    all = soup.select('item')
    chargespot_list = []

    sido_n = request.GET.get('sido')
    goo_n =  request.GET.get('goo')
    search_str = '서울특별시'

    if sido_n and goo_n:
        search_str = sido_n + ' ' + goo_n

    for tag in all:
        if search_str in str(tag.select_one('addr').text):
            chargespot = {"statNm" : "" , "address" : "","lat" : "" , "lng" : "", "chger_id" : "" ,
                         "chger_type" : "", "use_time" : "", "busi_nm": "", "busi_call" : "",
                         "stat" : "", }
            chargespot["statNm"] = str(tag.select_one('statNm').text)
            chargespot["address"] = str(tag.select_one('addr').text)
            chargespot["lat"] = str(tag.select_one('lat').text)
            chargespot["lng"] = str(tag.select_one('lng').text)
            chargespot["chger_id"] = str(tag.select_one('chgerId').text)
            #충전기 타입 입력
            # if str(tag.select_one("chgerType").text) in ['01', '04', '05']:
            #     chargespot["chgertype"] = "DC"
            # elif str(tag.select_one("chgerType").text) in ['02', '07'] :
            #     chargespot["chgertype"] = "AC"
            # elif str(tag.select_one("chgerType").text) in ['03', '06'] :
            #     chargespot["chgertype"] = "DC + AC"
            chargespot["chagertype"] = str(tag.select_one('chgerType').text)
            
            chargespot["use_time"] = str(tag.select_one('useTime').text)
            chargespot["busi_nm"] = str(tag.select_one('busiNm').text)
            chargespot["busi_call"] = str(tag.select_one('busiCall').text)
            #충전기 상태 입력
            if str(tag.select_one('stat').text) in ['2', '3']:
                chargespot["stat"] = "사용 가능"
            elif str(tag.select_one('stat').text) in ['4', '5']:
                chargespot["stat"] = "사용 불가"
            else:
                chargespot["stat"] = "미확인"
            chargespot["power_type"] = str(tag.select_one('powerType').text)
            chargespot_list.append(chargespot)

    return JsonResponse(chargespot_list, safe=False)

def index(request):
    return render(request,'map/index.html')
