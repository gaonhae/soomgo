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
import subprocess

subprocess.Popen(r'C:/Program Files/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/chrometemp"') # 디버거 크롬 구동


#설정을 위한 변수
yymmddInput = input("\n원하시는 연, 월, 일을 yymmdd와 같은 형식으로 입력해주세요 (ex.220403) : ") 
cosInput = input("원하시는 코스를 예시와 같은 형식으로 입력해주세요 (ex.썬) : ") 
timeInput = input("원하시는 시간을 예시와 같은 형식으로 입력해주세요 (ex.06:47) : ")


#브라우저, 매크로 설정
server = 'https://www.sunvalley.co.kr/member/login?returnURL=/reservation/golf'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none" 
URL = 'https://www.sunvalley.co.kr/member/login?returnURL=/reservation/golf'

#입력값 편집
yymmddInput = '20' + yymmddInput
editedtime= timeInput[0:2] + timeInput[3:5]

#브라우저 실행
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=1000)


#간편로그인

userid = driver.find_element_by_xpath('//*[@id="usrId"]')
userid.send_keys("31402500")

userpassword = driver.find_element_by_xpath('//*[@id="usrPwd"]')
userpassword.send_keys('2347812')


#설정한 시간이 될 때까지 대기
#for i in range(1, 999999):
#    date = urllib.request.urlopen(server).headers['Date'][5:-4]
#    hour = date[12:14]
#    min = date[15:17]
#    sec = date[18:]
#    if(sec == '00' and min == '00' and hour == '00'): #시간의 경우 원하는 시간 -9로 설정하면 됨. 지금의 경우 9시를 설정한 결과
#        break
#    print(f'{str(int(hour)+9)}시 {min}분 {sec}초')


time.sleep(10)

#매크로 진행
driver.refresh()

driver.find_element_by_xpath('//*[@id="selectCoIdJ21"]').click()

driver.execute_script("golfConfirm('{}','{}','1','{}','{}','18홀','','','FEEC92C302FE9A58')".format(yymmddInput, editedtime, cosInput, timeInput))



time.sleep(10000)
