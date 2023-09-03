#가변인자 함수
def football(name,team,*position):
    print("이름 : {0}\t소속팀 :{1}\t".format(name,team),end="포지션 :")
    for i in position:
        print(i,end=" ")
    print()

football("손흥민","토트넘","레프트윙","공격수","한국인","주장")
football("이강인","PSG","공미","중미","슛돌이")
