from selenium import webdriver
import pyautogui
from bs4 import BeautifulSoup
import time
from datetime import datetime
 
start = "송천고"
finish = "소래포구역"
data = []
 
driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://map.naver.com/v5/directions/-/-/-/mode?c=14107103.1786139,4494701.9630842,15,0,0,0,dh')
delay = 3
driver.implicitly_wait(delay)
driver.find_element_by_xpath('//*[@id="intro_popup_close"]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[3]/a').click()
driver.implicitly_wait(5)
driver.find_element_by_id('directionStart').send_keys(start)
time.sleep(0.02)
pyautogui.press('enter')
time.sleep(0.3)
driver.find_element_by_id('directionGoal').send_keys(finish)
time.sleep(0.02)
pyautogui.press('enter')
time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[2]/button[3]').click()
time.sleep(0.4)    
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
 
score_result = soup.find('div', {'class': 'summary_box'})
 
score_result = str(score_result)
times, length = score_result.split("추천", 1)
 
times = times.split(">",2)
times = times[2]
times = times.split("<",1)
times = times[0]
 
length = length.split(">",4)
length = length[4]
length = length.split("<",1)
length = length[0]
#print("거리 : " + length + "   /   소요예상시간 : " + times)
times_ff = times
driver.close()
 
now_hour = datetime.today().strftime("%H")
now_min = datetime.today().strftime("%M")
 
now_time = int(now_hour) * 60 + int(now_min)
if '시간' in times:
    times = times.split("시간",1)
    times_hour = times[0]
    times_hour = times_hour.replace("시간","")
    times_min = times[1]
    times_min = times_min.replace(" ","")
    times_min = times_min.replace("분","")
else:
    times = times.replace(" ","")
    times_min = times.replace("분","")
    times_hour = '0'
    
times_hour = str(times_hour)
times_min = str(times_min)
 
times_f = int(times_hour)*60 + int(times_min)
 
time_sum = times_f + now_time
 
time_f_hour = int(time_sum/60)
time_f_min = time_sum % 60
 
if time_f_hour >= 24:
    time_f_hour = time_f_hour - 24
    
    
print("거리 : " + length + "   /   예상소요시간 : " + times_ff + "   /   현재출발시 예상도착시간 : " + str(time_f_hour) + "시 " + str(time_f_min) + "분")
