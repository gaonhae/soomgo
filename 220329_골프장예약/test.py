from datetime import datetime
from timeit import timeit
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

yymmddInput = input("\n원하시는 연, 월, 일을 yymmdd와 같은 형식으로 입력해주세요 (ex.220403) : ") 
cosInput = input("원하시는 코스를 예시와 같은 형식으로 입력해주세요 (ex.썬) : ") 
timeInput = input("원하시는 시간을 예시와 같은 형식으로 입력해주세요 (ex.06:47) : ")
editedtime= timeInput[0:2] + timeInput[3:5]

server = 'https://www.sunvalley.co.kr/member/login?returnURL=/reservation/golf'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none" 
URL = 'https://www.sunvalley.co.kr/member/login?returnURL=/reservation/golf'

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=1000)

time.sleep(30)

driver.execute_script("golfConfirm('{}','{}','1','{}','{}','18홀','','','FEEC92C302FE9A58')".format(yymmddInput, editedtime, cosInput, timeInput))