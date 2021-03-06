from datetime import datetime
from urllib.parse import uses_relative
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
import os

#유저 입력 (날짜, 캠핑존, 자리, 기간, 소인, 대인)
# userMonth = input('\n예약을 원하시는 월을 입력해주세요 (ex. 6월의 경우 6, 11월의 경우 11) : ')
# userDate = input('\n원하시는 날짜의 좌표를 입력해주세요 (ex. 2022년 6월 22일의 경우 4,4) : ')
# print()
# print("     1 : 06:00 ~ 08:00")
# print("     2 : 08:00 ~ 10:00")
# print("     3 : 10:00 ~ 12:00")
# print("     4 : 12:00 ~ 14:00")
# print("     5 : 14:00 ~ 16:00")
# print("     6 : 16:00 ~ 18:00")
# print("     7 : 18:00 ~ 20:00")
# print("     8 : 20:00 ~ 22:00")
# userTime = input('\n예약을 원하시는 시간의 번호를 입력해주세요. : ')

#브라우저 설정
options = webdriver.ChromeOptions()
options.add_argument("no-sandbox") 
options.add_argument("disable-gpu") 
options.add_argument("--lang=ko_KR") 
options.add_argument( 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none" 
URL = "https://lakewood.co.kr/reservation/golf"
# URL = "https://online.igangdong.or.kr/rent/sports_rent_month_real.asp?SITE_CD=10017&PART_CD=1001&PLACE_CD=1005&d=m&F_Year=2022&F_Month=" + userMonth+ "&F_Day=21"

#입력정보편집



#브라우저 실행
driver = webdriver.Chrome('E:\CODING\soomgo\220625_레이크우드cc', options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=1000)

#로그인 후 사전 진입
driver.find_element_by_xpath('//*[@id="usrId"]').send_keys("wsmed")#아이디 입력
driver.find_element_by_xpath('//*[@id="usrPwd"]').send_keys("3379")#비밀번호 입력
driver.find_element_by_xpath('//*[@id="fnLogin"]').click()#로그인 버튼 누르기
Alert(driver).accept()#유재훈님 환영합니다
driver.find_element_by_xpath('//*[@id="A20220630"]/a').click()#6월 30일 누르기
driver.find_element_by_xpath('//*[@id="tabCourseALL"]/div[2]/div/table/tbody/tr[1]/td[5]/button').click()#산길 신청 누르기
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/table/tbody/tr/td[6]/a/img').click()#대관신청 누르기
# driver.find_element_by_xpath('//*[@id="agree1"]').click()#동의 누르기
# driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/form/div/table/tbody/tr[3]/td[2]/button').click()#확인 누르기

# #설정한 시간이 될 때까지 대기
# for i in range(1, 999999):
#    date = urllib.request.urlopen(URL).headers['Date'][5:-4]
#    hour = date[12:14]
#    min = date[15:17]
#    sec = date[18:]
#    if(sec == '00' and min == '00' and hour == '00'): #시간의 경우 원하는 시간 -9로 설정하면 됨. 지금의 경우 9시를 설정한 결과
#        break
#    print(f'{str(int(hour)+9)}시 {min}분 {sec}초')

# driver.refresh()
# driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[' + str(int(y)+1) +']/td[' + x  + ']/table/tbody/tr/td[1]/font/a/img').click()#날짜 선택
# driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[' + str(int(userTime)+1) + ']/td[1]/input').click()#시간 선택
# driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[2]/tbody/tr/td/form/table[2]/tbody/tr/td/a[1]/img').click()#등록버튼 누르기
# Alert(driver).accept()#등록확인


# driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr/td/a[1]/img').click()#최종등록누르기
# Alert(driver).accept()#최종등록확인
# time.sleep(1000)
# driver.refresh()

# Alert(driver).accept()#할인확인
