from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
import urllib.request


#유저 입력 (날짜, 캠핑존, 자리, 기간, 소인, 대인)
userdate = input('예약을 원하시는 월을 입력해주세요 (ex. 6월의 경우 06, 11월의 경우 11) : ')
userwhere = input('원하시는 날짜의 좌표를 입력해주세요 (ex. 2022년 5월 18일의 경우 4,3) : ')
usercarornormal = input('자동차야영장을 원하실 경우 1, 일반야영장을 원하실 경우 2를 입력해주세요. : ')
usersite = input('예약을 원하시는 자리의 번호를 적어주세요 (ex. 44) : ')
usertime = input('몇 박을 예약하실 건지 입력해주세요 (1박 2일의 경우 1, 2박 3일은 2 입력) : ')

#브라우저 설정
options = webdriver.ChromeOptions()
options.add_argument("no-sandbox") 
options.add_argument("disable-gpu") 
options.add_argument("--lang=ko_KR") 
options.add_argument( 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none" 
URL = "https://camp.xticket.kr/web/main?shopEncode=0d1fe2a656f145151b3a890a13a0171d61db84b1a5dc4b35d3b1d4bd938c381d"



#입력정보편집
normalseat = "0" + str(int(usersite) + 2009981)
carseat = "0" + str(int(usersite) + 1010000)
date = userdate[2:4]
moremonth = int(userdate[0:2]) - int(time.strftime('%m', time.localtime(time.time())))


#브라우저 실행
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=1000)

#설정한 시간이 될 때까지 대기
# for i in range(1, 999999):
#     now = time.strftime('%H%M%S', time.localtime(time.time()))
#     if( now == 110000): 
#         break
#     print(now[0:2],시 , now[2,4],분 , now[4,6],초 )


driver.refresh()
driver.find_element_by_xpath('//*[@id="notice_layer_274"]/div/div/div/fieldset/ul/li/button/img').click()#경고창1
driver.find_element_by_xpath('//*[@id="notice_layer_784"]/div/div/div/fieldset/ul/li/button/img').click()#경고창2
driver.find_element_by_xpath('//*[@id="login_id"]').send_keys("ttrat03")#아이디
driver.find_element_by_xpath('//*[@id="login_passwd"]').send_keys("tqlalf3847!!")#비번
driver.find_element_by_xpath('//*[@id="header"]/div[2]/fieldset/form/ul[1]/li[3]/a/img').click()#로그인
for i in range(moremonth):
    driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[1]/div[1]/ul[2]/li[2]/a').click()#다음월로 넘어가기
time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="calendarTable"]/tbody/tr[' + str(int(userwhere[2])+1) + ']/td[' + userwhere[0] + ']/a').click()#날짜 선택
driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/button').click()#n박 옵션 누르기
if (usertime == "1"):
    driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/ul/li[1]/a').click()#1박 누르기
elif (usertime == "2"):
    driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/ul/li[2]/a').click()#2박 누르기
if(usercarornormal == "1"):
    driver.find_element_by_xpath('//*[@id="자동차야영장"]').click()#자동차야영장선택
    driver.find_element_by_xpath('//*[@id="' + carseat +'"]').click()#자리선택
elif (usercarornormal == "2"):
    driver.find_element_by_xpath('//*[@id="일반야영장"]').click()#일반야영장선택
    driver.find_element_by_xpath('//*[@id="' + normalseat +'"]').click()#자리선택
driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/p/a/img').click()#예매하기
time.sleep(1000)
driver.refresh()

# Alert(driver).accept()#할인확인
