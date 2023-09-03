from random import *

com = randint(1, 3)
choices = ['가위', '바위', '보']
saram = int(input("1.가위 2.바위 3.보 : ")) - 1

print(f"사람 : {choices[saram]}", end="  ")
print(f"컴퓨터 : {choices[com - 1]}")

if saram == com - 1:
    print("비기셨습니다")
elif (saram + 1) % 3 == com - 1:
    print("컴퓨터가 이겼습니다")
else:
    print("사람이 이겼습니다")