me=input("1:가위, 2:바위, 3:보를 입력하세요. 숫자만 입력하세요")
from random import *
com=randint(1,3)

print(com)

if str(com)==me:
    print("비겼습니다.")
elif com==1 and me=="2" or com==2 and me=="3" or com==3 and me=="1":
    print("이겼습니다.")
else :
    print("졌습니다.")

    
