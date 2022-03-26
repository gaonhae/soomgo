from datetime import datetime
from http import cookies
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

userInput = input("원하시는 연월일을 입력하여 주십시오 : (ex 20220401)")
boat = input('원하시는 배를 선택해주세요 : (ex 스텔스호)')
fishcode = ""

print('현재 고를 수 있는 낚시의 종류는 다음과 같습니다')

if( boat == '스텔스호'):
    print('광어다운샷')
    boat = 1325
elif( boat == '전투호'):
    print('광어다운샷')
    boat = 1330
elif( boat == '이범호'):
    print('광어다운샷')
    boat = 1340
elif( boat == '대박피싱호'):
    print('중내만어초우럭')
    boat = 1329
elif( boat == '투지호'):
    print('봄쭈꾸미')
    print('광어우럭다운샷')
    boat = 1341
elif( boat == '댓길이호'):
    print('우럭광어라이트지깅')
    boat = 3352
elif( boat == '팀배틀호'):
    print('봄쭈꾸미')
    print('광어다운샷')
    boat = 3154
else:
    print('값을 잘못 입력하셨습니다!')

fish = input('원하시는 낚시 종류를 선택해주세요 : (ex 광어다운샷)')

if( boat == 1325):
    fishcode = '//*[@id="PS14593"]'
elif( boat == 1330):
    fishcode = '//*[@id="PS14639"]'
elif( boat == 1340):
    fishcode = '//*[@id="PS110876"]'
elif( boat == 1329):
    fishcode = '//*[@id="PS14623"]'
elif( boat == 1341):
    if(fish == '봄쭈꾸미'):
        fishcode = '//*[@id="PS14683"]'
    elif(fish == '광어우럭다운샷'):
        fishcode = '//*[@id="PS14682"]'
    else:
        print('값을 잘못 입력하셨습니다!')
elif( boat == 3352):
    fishcode = '//*[@id="PS115745"]'
elif( boat == 3154):
    if(fish == '봄쭈꾸미'):
        fishcode = '//*[@id="PS118309"]'
    elif(fish == '광어다운샷'):
        fishcode = '//*[@id="PS114237"]'
    else:
        print('값을 잘못 입력하셨습니다!')

howManyPeople = input('인원을 설정하여주십시오 (ex 6) : ')

URL = 'https://www.muchangpo.kr/m/_core/module/reservation_boat_v3/m/popup.step1.php?date=' + userInput +'&PA_N_UID=' + str(boat)



driver = webdriver.Chrome()
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=5)

choose = driver.find_element_by_xpath(fishcode)
choose.click()

Select(driver.find_element_by_xpath('//*[@id="BI_IN"]')).select_by_visible_text(howManyPeople + '명')

fisherName = driver.find_element_by_xpath('//*[@id="insert_form"]/div[1]/div[2]/dl[8]/dd/input')
fisherName.send_keys('강창환')

payerName = driver.find_element_by_xpath('//*[@id="BI_BANK"]')
payerName.send_keys('강창환')

middleNum = driver.find_element_by_xpath('//*[@id="BI_TEL2"]')
middleNum.send_keys('4740')

lastNum = driver.find_element_by_xpath('//*[@id="BI_TEL3"]')
lastNum.send_keys('4671')

driver.find_element_by_xpath('//*[@id="insert_form"]/div[1]/div[5]/div[8]/label[1]/span').click()

driver.find_element_by_xpath('//*[@id="submit"]').click()

Alert(driver).accept()

#lastCheck = driver.find_element_by_xpath('//*[@id="submit"]').click()