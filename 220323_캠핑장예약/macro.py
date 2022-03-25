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

if(settingInput[0] == 'A' or settingInput[0] == 'a'):
    abc = 1
elif(settingInput[0] == 'B' or settingInput[0] == 'b'):
    abc = 2
elif(settingInput[0] == 'C' or settingInput[0] == 'c'):
    abc = 3

URL = 'https://camping.gtdc.or.kr/DZ_reservation/reserCamping_v3.php?xch=reservation&xid=camping_reservation&sdate=20' + yymmInput



driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=5)

agree = driver.find_element_by_xpath('//*[@id="posFrm"]/div[2]/button')
agree.click()

day = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[3]/div/div/table[2]/tbody/tr[' + ddInput[0] + ']/td[' + ddInput[2] + ']/ul/li[' + str(abc) + ']/button')
day.click()

where = driver.find_element_by_xpath('//*[@id="camping_zone"]/button[' + settingInput[2:4] +']')
where.click()


Select(driver.find_element_by_xpath('//*[@id="setPersion_Room' + settingInput[2:4] +'"]/td[4]/select')).select_by_visible_text(settingInput[4] + '명')

nextBtn = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[3]/div/div/div[6]/button[2]')
nextBtn.click()




