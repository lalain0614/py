from random import *

print(random())             #0.0~1.0 미만 출력
print(random()*10)          #0.0~10.0 미만 출력
print(int(random()*10))     #0~10 미만 출력
print(int(random()*10)+1)    #1~10 이하 출력

print(randrange(1,100))     #1~100미만 랜덤 출력(정수형)
print(randrange(1,100,3))   #1~100미만 랜덤(정수형,+3씩 증가) 1,4,7....
print(randint(1,10))        #1~10 이하 랜덤 출력
print(randint(1,100))       #1~100이하 랜덤 출력
