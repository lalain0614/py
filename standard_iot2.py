game_cnt={"2020년":998,"2021년":1567,"2022년":9999}
print(game_cnt.items())
for year,cnt in game_cnt.items():
    print(year,cnt)
    
for year,cnt in game_cnt.items():
    print(year.ljust(5),str(cnt).rjust(5)+"개 입니다.",sep="의 총 게임 개수는?")
    
for x in range(1,5):
    print("번호 : "+str(x).zfill(4)+"입니다.")
    #zfill 0으로 채우기
    