name1="손흥민"
shooting1=99
passing1=70
defenace1=50
run1=100

name2="이강인"
shooting2=94
passing2=100
defenace2=60
run2=83

print("슈팅 : {0}, 패스 : {1}, 수비 : {2}, 뜀박질 : {3}".format(shooting1,passing1,defenace1,run1))
print("슈팅 : {0}, 패스 : {1}, 수비 : {2}, 뜀박질 : {3}".format(shooting2,passing2,defenace2,run2))

def soccer_game(name, shooting):
    print("{0} 선수가 슛을 {1} 만큼의 능력치로 찼습니다.".format(name,shooting))
    
soccer_game(name1,shooting1)
soccer_game(name2,shooting2)

