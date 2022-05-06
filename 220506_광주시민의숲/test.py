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
# userdate = input('예약을 원하시는 날짜를 예시와 같이 입력해주세요 : (ex. 2022-04-25) ')
# userzone = input('예약을 원하시는 캠핑존의 이름 전체를 적어주세요 : (ex. 렌탈캠핑존A)')
# usersite = input('예약을 원하시는 자리의 번호를 적어주세요 : (ex. 18)')
# usersmall = input('예약하실 인원 중 소인은 몇 명인지 입력해주세요 : (ex. 2)')
# userbig = input('예약하실 인원 중 대인은 몇 명인지 입력해주세요 : (ex. 2)')

# if userzone == '평화캠핑존':
#     userzone = '2'
# elif userzone == '힐링캠핑존':
#     userzone = '3'
# elif userzone == '누리캠핑존':
#     userzone = '4'
# elif userzone == '에코캠핑존':
#     userzone = '5'
# elif userzone == '렌탈캠핑존A':
#     userzone = '6'
# elif userzone == '렌탈캠핑존B':
#     userzone = '7'
# elif userzone == '카라반존A':
#     userzone = '8'
# elif userzone == '카라반존B':
#     userzone = '9'
# elif userzone == '카라반존C':
#     userzone = '10'

#브라우저 설정
server = 'https://imjingakcamping.co.kr/'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none" 
URL = "https://www.sagewood.co.kr/yeosu/reservation/golf"

#브라우저 실행
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=1000)


#설정한 시간이 될 때까지 대기
# for i in range(1, 999999):
#     date = urllib.request.urlopen(server).headers['Date'][5:-4]
#     hour = date[12:14]
#     min = date[15:17]
#     sec = date[18:]
#     if(sec == '00' and min == '00' and hour == '01'): #시간의 경우 원하는 시간 -9로 설정하면 됨. 지금의 경우 10시를 설정한 결과
#         break
#     print(f'{str(int(hour)+9)}시 {min}분 {sec}초')


usertime = input('몇 시 할 겨??')
js = 'golfTimeSelect' + "('2022.05.25', '오동도', '" + usertime + "', '220,000', '1', 'N')"
a = "golfTimeSelect('2022.05.25', '오동도', '0656', '220,000', '1', 'N')"
print(js)
# print(a)

time.sleep(5)


driver.find_element_by_xpath('//*[@id="golf_step-01"]/div[1]/div/div[1]/table[1]/tbody/tr[4]/td[4]/div').click()
driver.find_element_by_xpath('//*[@id="rec_search"]').click()
driver.execute_script(js)
# driver.execute_script(a)
# driver.execute_script('"golfTimeSelect'+"('2022.05.25', '오동도', '"+usertime+"', '220,000', '1', 'N')"+'"')
# driver.execute_script("golfTimeSelect('2022.05.25', '오동도', '0656', '220,000', '1', 'N')")

"golfTimeSelect('2022.05.25', '오동도', '0656', '220,000', '1', 'N')"

time.sleep(100000)

# driver.refresh()
# driver.find_element_by_xpath('//*[@id="contents"]/div/div[8]/div[1]/button['+ userzone +']').click()#캠핑존 선택
# driver.find_element_by_xpath('//*[@id="site_hl"]/div['+usersite+']/label').click()#자리선택
# Select(driver.find_element_by_xpath('//*[@id="reservForm"]/div[1]/div/table/tbody/tr[1]/td[3]/select')).select_by_value(usertime)#일수선택
# Select(driver.find_element_by_xpath('//*[@id="reservForm"]/div[1]/div/table/tbody/tr[1]/td[4]/select')).select_by_value(userbig)#대인선택
# Select(driver.find_element_by_xpath('//*[@id="reservForm"]/div[1]/div/table/tbody/tr[1]/td[5]/select')).select_by_value(usersmall)#소인선택
# driver.find_element_by_xpath('//*[@id="contents"]/div/div[9]/div[3]/button').click()#중간확인
# driver.find_element_by_xpath('//*[@id="order_info"]/div[2]/div[1]/div[1]/label').click()#지역주민할인
# Alert(driver).accept()#할인확인
# driver.find_element_by_xpath('//*[@id="order_info"]/fieldset/div/dl[1]/dd[1]/input').send_keys('정연일')#이름
# driver.find_element_by_xpath('//*[@id="order_info"]/fieldset/div/dl[1]/dd[2]/input').send_keys('01023597578')#연락처
# driver.find_element_by_xpath('//*[@id="order_info"]/fieldset/div/dl[2]/dd/input').send_keys('icecon@naver.com')#이메일
# driver.find_element_by_xpath('//*[@id="order_info"]/fieldset/div/dl[3]/dd/input').send_keys('840128')#생년월일
# driver.find_element_by_xpath('//*[@id="order_info"]/fieldset/div/dl[4]/dd/input').send_keys('18가1734')#차량번호
# driver.find_element_by_xpath('//*[@id="order_info"]/div[12]/label').click()#환불규정동의
# driver.find_element_by_xpath('//*[@id="order_info"]/div[14]/label').click()#개인정보동의
# driver.find_element_by_xpath('//*[@id="order_info"]/div[15]/label').click()#전체동의
# driver.find_element_by_xpath('//*[@id="order_info"]/div[16]/button').click()#예약하기