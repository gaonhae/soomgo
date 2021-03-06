#시간을 어떻게 선택할 것인가
#bad gateway를 어떻게 대처할 것인가

from datetime import datetime
from select import select
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

#아이디와 비밀번호 읽어오기
f = open("ID&PW.txt", "r")
id = f.readline().rstrip()
pw = f.readline().rstrip()
f.close()

#유저 입력 (날짜, 캠핑존, 자리, 기간, 소인, 대인)
userServerTime = ""
userServerTime = input('\n서버 시간 옵션을 사용하시려면 엔터를, 사용하지 않고 바로 실행하시려면 1을 입력해주세요. : ')
userMonth = input('\n예약을 원하시는 월을 입력해주세요 (ex. 6월의 경우 6, 11월의 경우 11) : ')
userDate = input('\n원하시는 날짜의 좌표를 입력해주세요 (ex. 2022년 6월 22일의 경우 4,4) : ')
userWhere = input('\n예약을 원하시는 시설과 코트를 입력해주세요 (ex. 강일테니스장 7번 코트의 경우 2,7) : ')
userTime = input('\n예약을 원하시는 시간의 번호를 입력해주세요. : ')


#브라우저 설정
options = webdriver.ChromeOptions()
options.add_argument("no-sandbox") 
options.add_argument("window-size=1920x1080") 
# options.add_argument("headless") 
options.add_argument("disable-gpu") 
options.add_argument("--lang=ko_KR") 
options.add_argument( 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
options.add_argument("--blink-setting=imagesEnable=false")
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "none" #페이지 완전 로딩 대기할 거야? 
URL = "https://online.igangdong.or.kr//member/login.asp"


#입력정보편집
x = userDate[0] 
y = userDate[2] 
siteValue =""
partValue = ""
courtValue = ""
userSite = userWhere[0]
userCourt = userWhere[2:]
if(userSite == '1'):
    siteValue = '10017'
    partValue = '1001'
    userCourt = "100" + userCourt
    courtValue = userCourt[3] + "코트"
elif(userSite == '2'):
    siteValue = '10019'
    if(int(userCourt) >= 5):
        partValue = '1002'
        if(userCourt == "5"):
            userCourt = "1005"
            courtValue = "5코트"
        elif(userCourt == "6"):
            userCourt = "1007"
            courtValue = "6코트"
        elif(userCourt == "7"):
            userCourt = "1008"
            courtValue = "7코트"
        elif(userCourt == "8"):
            userCourt = "1009"
            courtValue = "8코트"
        elif(userCourt == "9"):
            userCourt = "1010"
            courtValue = "9코트"
        elif(userCourt == "10"):
            userCourt = "1010"
            courtValue = "10코트"
    else:
        partValue = '1001'
        userCourt = "100" + userCourt
        courtValue = userCourt[3] + "코트"
else:
    print("입력값이 잘못되었습니다. 프로그램을 종료하신 후 다시 입력해주세요.")


#브라우저 실행
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=1000)

#로그인 후 사전 진입
driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[6]/td/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/table/tbody/tr[1]/td[2]/input').send_keys(id)#아이디 입력
driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[6]/td/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/table/tbody/tr[3]/td[2]/input').send_keys(pw)#비밀번호 입력
driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[6]/td/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/a/img').click()#로그인 버튼 누르기
driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/table/tbody/tr/td[6]/a/img').click()#대관신청 누르기
driver.find_element(By.XPATH,'//*[@id="agree1"]').click()#동의 누르기
driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/form/div/table/tbody/tr[3]/td[2]/button').click()#확인 누르기
driver.get("https://online.igangdong.or.kr/rent/sports_rent_month_real.asp?SITE_CD=" + siteValue + "&PART_CD="+ partValue +"&PLACE_CD=" + userCourt + "&d=m&F_Year=2022&F_Month=" + userMonth + "&F_Day=29")



#설정한 시간이 될 때까지 대기
for i in range(1, 999999):
    if(userServerTime == '1'):
        break
    date = urllib.request.urlopen(URL).headers['Date'][5:-4]
    hour = date[12:14]
    min = date[15:17]
    sec = date[18:]
    if(sec == '00' and min == '00' and hour == '01'): #시간의 경우 원하는 시간 -9로 설정하면 됨. 지금의 경우 10시를 설정한 결과
       break
    print(f'{str(int(hour)+9)}시 {min}분 {sec}초')




flag = True
while(flag):
    driver.refresh()
    driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[' + str(int(y)+1) +']/td[' + x  + ']/table/tbody/tr/td[1]/font/a/img').click()#날짜 선택
    time.sleep(0.5)
    if(driver.current_url == 'https://online.igangdong.or.kr/rent/rent_step1.asp'):
        flag = False

flag = True
while(flag):
    driver.refresh()
    driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[' + str(int(userTime)+1) + ']/td[1]/input').click()#시간 선택
    driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[2]/tbody/tr/td/form/table[2]/tbody/tr/td/a[1]/img').click()#등록버튼 누르기
    Alert(driver).accept()#등록확인
    time.sleep(0.5)
    if(driver.current_url == 'https://online.igangdong.or.kr/rent/rent_step2.asp'):
        flag = False


flag = True
while(flag):
    driver.refresh()
    # Alert(driver).accept()#찾고 있는 페이지에서 사용자가 입력한 정보를 사용했습니다. 해당 페이지로 돌아가면 기존 작업을 반복할 수 있습니다. 계속하시겠습니까?
    driver.find_element(By.XPATH,'//*[@id="form1"]/table[2]/tbody/tr/td/a[1]/img').click()#최종등록누르기
    Alert(driver).accept()#최종등록확인
    time.sleep(0.5)
    if(driver.current_url == 'https://online.igangdong.or.kr/member/my_rent.asp'):
        flag = False

date = urllib.request.urlopen(URL).headers['Date'][5:-4]
hour = date[12:14]
min = date[15:17]
sec = date[18:]
driver.save_screenshot('screenshot_'+f'{str(int(hour)-24)}시 {min}분 {sec}초'+'.png')
time.sleep(1000)
driver.refresh()

# Alert(driver).accept()#할인확인