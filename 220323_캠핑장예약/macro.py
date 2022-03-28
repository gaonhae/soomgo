from datetime import datetime
from selenium import webdriver
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


#설정을 위한 변수
yymmInput = input("\n원하시는 연, 월을 yymm과 같은 형식으로 입력하여주세요 (ex.2204) : ") 
ddInput = input("원하시는 날짜의 좌표를 (x,y)형식으로 입력해주세요 ex(3,4): ")
settingInput = input("원하시는 지역, 자리, 인원을 예시와 같은 형식으로 입력하여주세요 (ex.A1086) : ")
seatNum = int(settingInput[1:4])
seatBtnNum = settingInput[2:4]


#브라우저, 매크로 설정
server = 'http://camping.gtdc.or.kr'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none" 


#입력값 편집
if(settingInput[0] == 'A' or settingInput[0] == 'a'):
    abc = 1
    seatNum -= 100
    if(seatNum >= 42):
        seatNum += 106
elif(settingInput[0] == 'B' or settingInput[0] == 'b'):
    abc = 2
    seatNum -= 159
elif(settingInput[0] == 'C' or settingInput[0] == 'c'):
    abc = 3
    seatNum -= 218
elif(settingInput[0] == 'D' or settingInput[0] == 'd'):
    abc = 4
    if(seatNum == 709):
        seatNum += 1
    seatNum -= 533
elif(settingInput[0] == 'E' or settingInput[0] == 'e'):
    abc = 5
    seatNum -= 380    
if(seatNum < 10):
    seatNum = int(settingInput[3:4])


#url 설정
URL = 'https://camping.gtdc.or.kr/DZ_reservation/reserCamping_v3.php?xch=reservation&xid=camping_reservation&sdate=20' + yymmInput

#브라우저 실행
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=1000)

#설정한 시간이 될 때까지 대기
for i in range(1, 999999):
    date = urllib.request.urlopen(server).headers['Date'][5:-4]
    hour = date[12:14]
    min = date[15:17]
    sec = date[18:]
    if(sec == '00' and min == '00' and hour == '01'):
        break
    print(f'{str(int(hour)+9)}시 {min}분 {sec}초')

#매크로 진행

agree = driver.find_element_by_xpath('//*[@id="posFrm"]/div[2]/button')
agree.click()


day = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[3]/div/div/table[2]/tbody/tr[' + ddInput[0] + ']/td[' + ddInput[2] + ']/ul/li[' + str(abc) + ']/button')
day.click()

where = driver.find_element_by_xpath('//*[@id="camping_zone"]/button[' + seatBtnNum +']')
where.click()

Select(driver.find_element_by_xpath('//*[@id="setPersion_Room' + str(seatNum) +'"]/td[4]/select')).select_by_visible_text(settingInput[4] + '명')

nextBtn = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[3]/div/div/div[6]/button[2]')
nextBtn.click()
