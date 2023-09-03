cnt=0
def bouns_coffee(cf_cnt):
    global cnt
    cnt += cf_cnt
    if cnt>10:
        print("쿠폰 10개 보너스 커피 제공")    
        cnt-=10
    else:
        print("현재 쿠폰 보유량은 {0}입니다.".format(cnt))

while 1 :
    coffee_cnt=int(input("커피 수량을 입력하세요"))
    bouns_coffee(coffee_cnt)
    
