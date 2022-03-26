from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

yymmInput = input("\n원하시는 연, 월을 yymm과 같은 형식으로 입력하여주세요 (ex.2204) : ") 
ddInput = input("원하시는 날짜의 좌표를 (x,y)형식으로 입력해주세요 ex(3,4): ")
settingInput = input("원하시는 지역, 자리, 인원을 예시와 같은 형식으로 입력하여주세요 (ex.A1086) : ")
seatNum = int(settingInput[1:4])
seatBtnNum = settingInput[2:4]

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



URL = 'https://camping.gtdc.or.kr/DZ_reservation/reserCamping_v3.php?xch=reservation&xid=camping_reservation&sdate=20' + yymmInput



driver = webdriver.Chrome("E:/CODING/@Soomgo/220323_캠핑장예약/chromedriver.exe")
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=5)

agree = driver.find_element_by_xpath('//*[@id="posFrm"]/div[2]/button')
agree.click()

day = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[3]/div/div/table[2]/tbody/tr[' + ddInput[0] + ']/td[' + ddInput[2] + ']/ul/li[' + str(abc) + ']/button')
day.click()

where = driver.find_element_by_xpath('//*[@id="camping_zone"]/button[' + seatBtnNum +']')
where.click()


Select(driver.find_element_by_xpath('//*[@id="setPersion_Room' + str(seatNum) +'"]/td[4]/select')).select_by_visible_text(settingInput[4] + '명')

nextBtn = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[3]/div/div/div[6]/button[2]')
nextBtn.click()



#a 구역은 142번부터 +6 (141번은 41, 142번은 148)
#b 구역은 201번부터 42 ()
#c 구역은 301번부터 82 ()
#d 구역은 701번부터 168, 709번은 177
#e 구역은 502번부터 122, -380
