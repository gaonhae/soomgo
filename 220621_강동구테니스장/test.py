userWhere = input('\n예약을 원하시는 시설과 코트를 입력해주세요 (ex. 강일테니스장 7번 코트의 경우 2,7) : ')



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

print(userCourt)
print(courtValue)
