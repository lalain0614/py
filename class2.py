class soccer_player:
    def __init__(self,name,shooting,passing,defance,run):
        self.name=name
        self.shooting = shooting
        self.passing = passing
        self.defance = defance
        self.run = run
        
        print("{0}선수가 슛을 {1}만큼의 능력치로 찼습니다.".format(self.name,self.shooting))
        print("슈팅 : {0}, 패스 : {1}".format(self.shooting,self.passing))
        print("수비 : {0}, 뜀박질 : {1}".format(self.defance,self.run))

player1 = soccer_player("손흥민",96,89,77,100)
player2 = soccer_player("이강인",89,94,83,88)