num=12
print("{0:>5}".format(num))#전체 자리를 5칸으로 넣음
print("{0:<5}".format(num))
su_1=12
su_2=-12
print("{0:>+5}".format(su_1))# +를 넣으면 부호를 표시
print("{0:>+5}".format(su_2))

buho=5
print("{0:*>10}".format(buho))#빈칸에 *에 들어감
buho+=10
print("{0:*>10}".format(buho))

price=123456789
print("{0:,}".format(price))#천단위 구분
