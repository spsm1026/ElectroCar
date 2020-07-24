from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path
# from . import data
from django.template import loader
from bs4 import BeautifulSoup
from .models import Sido, Goo, Carcharger
import smtplib
from email.mime.text import MIMEText

from selenium import webdriver as wd
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
from bs4 import BeautifulSoup
from datetime import datetime

import re


def add(request):
    input_address = request.GET.get('input_address')
    marker_address = request.GET.get('marker_address')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

   
    # driver.close() #메모리 정리

    start = input_address 
    finish = marker_address
    data = []



    driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)

    driver.get('https://map.naver.com/v5/directions/-/-/-/mode?c=14107103.1786139,4494701.9630842,15,0,0,0,dh')
    delay = 3
    driver.implicitly_wait(delay)
    # driver.find_element_by_xpath('//*[@id="intro_popup_close"]/span').click()
    # driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[2]/a').click()
    driver.implicitly_wait(5)
    el = driver.find_element_by_id('directionStart0')
    el.send_keys(start)
    time.sleep(0.02)
    el.send_keys(Keys.ENTER)
    time.sleep(0.2)
    al = driver.find_element_by_id('directionGoal1')
    al.send_keys(finish)
    time.sleep(0.02)
    al.send_keys(Keys.ENTER)
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[2]/button[3]').click()
    time.sleep(0.3)

    km = driver.find_element_by_css_selector('div.inner_scroll span.summary_text').text
    
    return JsonResponse({'km' : km}, safe=False)

def add2(request):
    input_address1 = request.GET.get('input_address1')
    input_address2 = request.GET.get('input_address2')
    input_car = request.GET.get('input_car')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

    driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)

    # driver.close() #메모리 정리
    

    start = input_address1
    finish = input_address2
    data = []

    load = "로딩 중..."

    driver.get('https://map.naver.com/v5/directions/-/-/-/mode?c=14107103.1786139,4494701.9630842,15,0,0,0,dh')
    delay = 3
    driver.implicitly_wait(delay)
    # driver.find_element_by_xpath('//*[@id="intro_popup_close"]/span').click()
    # driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[2]/a').click()
    driver.implicitly_wait(5)
    el = driver.find_element_by_id('directionStart0')
    el.send_keys(start)
    time.sleep(0.02)
    el.send_keys(Keys.ENTER)
    time.sleep(0.2)
    al = driver.find_element_by_id('directionGoal1')
    al.send_keys(finish)
    time.sleep(0.02)
    al.send_keys(Keys.ENTER)
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[2]/button[3]').click()
    time.sleep(0.3)

    km2 = driver.find_element_by_css_selector('div.inner_scroll span.summary_text').text
    km2 = km2[:-2]
    km2 = float(km2)

    if input_car == "기본연비":
        cal_re = ( 255.7 / 5.5 ) * km2
    elif input_car == "현대 코나":
        cal_re = ( 255.7 / 5.6 ) * km2
    elif input_car == "기아 레이":
        cal_re = ( 255.7 / 5.0 ) * km2
    elif input_car == "기아 쏘울":
        cal_re = ( 255.7 / 5.4 ) * km2
    elif input_car == "현대 아이오닉":
        cal_re = ( 255.7 / 6.3 ) * km2
    elif input_car == "쉐보레 볼트":
        cal_re = ( 255.7 / 5.5 ) * km2
    elif input_car == "기아 니로":
        cal_re = ( 255.7 / 5.3 ) * km2
    elif input_car == "르노삼성 SM3Z.E.":
        cal_re = ( 255.7 / 4.5 ) * km2
    elif input_car == "BMW i3":
        cal_re = ( 255.7 / 5.4 ) * km2
    elif input_car == "쉐보레 스파크":
        cal_re = ( 255.7 / 6.0 ) * km2
    elif input_car == "테슬라 모델X":
        cal_re = ( 255.7 / 3.4 ) * km2
    elif input_car == "테슬라 모델SP":
        cal_re = ( 255.7 / 3.8 ) * km2

    cal_re = int(cal_re)

    
    return JsonResponse({'cal_re' : cal_re }, safe=False)

def map(request):
    carcharger_list = Carcharger.objects.order_by('id')
    # sido_list = Sido.objects.order_by('sido_name')
    # seoul = Sido.objects.get(id=1)
    # goo_list = Goo.objects.filter(sido=seoul)

    return render(request, 'map/map.html', {'carcharger_list' : carcharger_list})

def map_data(request):
    url ='http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=%2FuulHEenTm5AaXHhdM5TCK3IG6AkNr5%2BQeE1QH1tBNBPYe%2FDSWYlpahKtXBwo7U4xn1T8pNhgH3t7zwTGljWqQ%3D%3D'
    res = requests.get(url)
    res.encoding = None
    print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    all = soup.select('item')
    chargespot_list = []

    sido_n = request.GET.get('sido')
    goo_n =  request.GET.get('goo')
    search_str = '서울특별시'

    if sido_n or goo_n:
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

def sendMail(from_email, to_email, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(from_email, 'mvewisjmzdhunusn') 
    msg = MIMEText(msg)
    msg['Subject'] = '가입인사'
    msg['To'] = to_email
    smtp.sendmail(from_email, to_email, msg.as_string())
    smtp.quit()

def sendMail_2(request):
    sendMail("22@gmail.com","22@gmail.com","완료 되었습니다.")
    return render(request, 'map/index.html','')
def test(request):
    return render(request,'map/test.html')
