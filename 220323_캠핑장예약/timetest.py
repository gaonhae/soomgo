import urllib.request
import time
 
month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

server = 'http://camping.gtdc.or.kr'



for i in range(1, 99999):
#    url = 'http://camping.gtdc.or.kr'
#    date = urllib.request.urlopen(url).headers['Date'][5:-4]
#    d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]
#    print(f'[{url}]의 서버시간\n{y}년 {m}월 {d}일 {str(int(hour)+9)}시 {min}분 {sec}초')
    date = urllib.request.urlopen(server).headers['Date'][5:-4]
    hour = date[12:14]
    min = date[15:17]
    sec = date[18:]
    print(f'{hour}시 {min}분 {sec}초')