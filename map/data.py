from bs4 import BeautifulSoup
import requests


url ='http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=s7Ytkl8dJDy32JsmhtlyMEGVjWPfEcBuXNnDCYQHitUBkHblPkhsXakF6aMhFf6NFOcxj6RFnuim5wTJUPNrkQ%3D%3D'
res = requests.get(url)
res.encoding = None
soup = BeautifulSoup(res.text, 'html.parser')
# print(res.text)
all = soup.select('item')
chargespot_list = []
for tag in all:
    chargespot = {"lat" : "" , "lng" : "" }
    chargespot["lat"] = tag.select_one('lat')
    chargespot["lng"] = tag.select_one('lng')
    chargespot_list.append(chargespot)







