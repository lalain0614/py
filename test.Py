import tkinter

window=tkinter.Tk()
window.geometry('1900x1100+0+0')
window.resizable(False,False)
window.title("부산 노선도")

frame1=tkinter.Frame(window,relief="solid",bd=3,height=200)
frame1.pack(side="top",fill="x")
frame2=tkinter.Frame(window,relief="solid",bd=3,width=1298,height=823)
frame2.pack(side="left",fill="both",expand=True)
frame3=tkinter.Frame(window,relief="solid",bd=3)
frame3.pack(side="right",fill="both",expand=True)

cnavas=tkinter.Canvas(frame2,width=1100,height=800)
cnavas.pack(side="bottom")

input1=tkinter.Entry(frame1)
input1.place(x=30,y=20,height=50)
input2=tkinter.Entry(frame1)
input2.place(x=30,y=80,height=50)


start=''
end=''


def fn1():
    global start
    global end
    start=input1.get()
    end=input2.get()
    
    cnavas.itemconfig(eval(start),fill="blue")
    cnavas.itemconfig(eval(end),fill="red")
           
    import copy
    import pandas as pd
    from datetime import datetime, timedelta
    from collections import defaultdict
    grade = pd.read_excel(r"C:\Users\대컴\Desktop\padas_프로젝트2.xlsx", sheet_name="1호선", skiprows="")
    grouped_data = defaultdict(dict)

    stations = grade['역명'].tolist()
    times = grade['시간'].tolist() 

    injup_station1 = grade['인접역1'].tolist()
    line_1 = grade['1역 호선'].tolist()
    soyo_time1 = grade['1역 소요시간'].tolist()

    injup_station2 = grade['인접역2'].tolist()
    line_2 = grade['2역 호선'].tolist()
    soyo_time2 = grade['2역 소요시간'].tolist()

    injup_station3 = grade['인접역3'].tolist()
    line_3 = grade['3역 호선'].tolist()
    soyo_time3 = grade['3역 소요시간'].tolist()

    injup_station4 = grade['인접역4'].tolist()
    line_4 = grade['4역 호선'].tolist()
    soyo_time4 = grade['4역 소요시간'].tolist()

    start_station = {}

    for i in range(len(stations)):
      station_data = {
         injup_station1[i] : soyo_time1[i],
         
      }
      if pd.notna(injup_station2[i]) and pd.notna(soyo_time2[i]):
         station_data[injup_station2[i]] = int(soyo_time2[i])
         

      if pd.notna(injup_station3[i]) and pd.notna(soyo_time3[i]):
         station_data[injup_station3[i]] = int(soyo_time3[i],)
         

      if pd.notna(injup_station4[i]) and pd.notna(soyo_time4[i]):
         station_data[injup_station4[i]] = int(soyo_time4[i])
         
      
      start_station[stations[i]] = station_data    
    
    routing ={}
    for place in start_station.keys():
      routing[place]={'shortestDist':0, 'route':[], 'visited':0}
      
    def visitPlace(visit):
      routing[visit]['visited'] = 1
      for togo, betweenDist in start_station[visit].items():
         toDist = routing[visit]['shortestDist'] + betweenDist
         if(routing[togo]['shortestDist']>=toDist) or not routing[togo]['route']:
               routing[togo]['shortestDist'] = toDist
               routing[togo]['route'] = copy.deepcopy(routing[visit]['route'])
               routing[togo]['route'].append(visit)
    visitPlace(start)    

    while 1:
      minDist = max(routing.values(), key=lambda x:x['shortestDist'])['shortestDist']
      toVisit =''
      for name, search in routing.items():
         if 0 < search['shortestDist'] <= minDist and not search['visited']:
               minDist = search['shortestDist']
               toVisit = name
      if toVisit == '':
         break
      visitPlace(toVisit)
    route_01=[]
    route_01=routing[end]['route']
    route_01.remove(route_01[0])
    for i in route_01:
       cnavas.itemconfig(eval(i),fill="black") 

def fn2():
    global start
    global end
    start=input1.get()
    end=input2.get()
    import copy
    import pandas as pd
    from datetime import datetime, timedelta
    from collections import defaultdict
    grade = pd.read_excel(r"C:\Users\대컴\Desktop\padas_프로젝트2.xlsx", sheet_name="1호선", skiprows="")
    grouped_data = defaultdict(dict)

    stations = grade['역명'].tolist()
    times = grade['시간'].tolist() 

    injup_station1 = grade['인접역1'].tolist()
    line_1 = grade['1역 호선'].tolist()
    soyo_time1 = grade['1역 소요시간'].tolist()

    injup_station2 = grade['인접역2'].tolist()
    line_2 = grade['2역 호선'].tolist()
    soyo_time2 = grade['2역 소요시간'].tolist()

    injup_station3 = grade['인접역3'].tolist()
    line_3 = grade['3역 호선'].tolist()
    soyo_time3 = grade['3역 소요시간'].tolist()

    injup_station4 = grade['인접역4'].tolist()
    line_4 = grade['4역 호선'].tolist()
    soyo_time4 = grade['4역 소요시간'].tolist()

    start_station = {}

    for i in range(len(stations)):
      station_data = {
         injup_station1[i] : soyo_time1[i],
         
      }
      if pd.notna(injup_station2[i]) and pd.notna(soyo_time2[i]):
         station_data[injup_station2[i]] = int(soyo_time2[i])
         

      if pd.notna(injup_station3[i]) and pd.notna(soyo_time3[i]):
         station_data[injup_station3[i]] = int(soyo_time3[i],)
         

      if pd.notna(injup_station4[i]) and pd.notna(soyo_time4[i]):
         station_data[injup_station4[i]] = int(soyo_time4[i])
         
      start_station[stations[i]] = station_data    
    
    routing ={}
    for place in start_station.keys():
      routing[place]={'shortestDist':0, 'route':[], 'visited':0}
      
    def visitPlace(visit):
      routing[visit]['visited'] = 1
      for togo, betweenDist in start_station[visit].items():
         toDist = routing[visit]['shortestDist'] + betweenDist
         if(routing[togo]['shortestDist']>=toDist) or not routing[togo]['route']:
               routing[togo]['shortestDist'] = toDist
               routing[togo]['route'] = copy.deepcopy(routing[visit]['route'])
               routing[togo]['route'].append(visit)
    visitPlace(start)    

    while 1:
      minDist = max(routing.values(), key=lambda x:x['shortestDist'])['shortestDist']
      toVisit =''
      for name, search in routing.items():
         if 0 < search['shortestDist'] <= minDist and not search['visited']:
               minDist = search['shortestDist']
               toVisit = name
      if toVisit == '':
         break
      visitPlace(toVisit)
    route_01=[]
    route_01=routing[end]['route']
    route_01.remove(route_01[0])
    for i in route_01:
       cnavas.itemconfig(eval(i),fill="snow") 
    cnavas.itemconfig(eval(start),fill="snow")
    cnavas.itemconfig(eval(end),fill="snow")
    input1.delete(0,10000)
    input2.delete(0,10000)




line_1= cnavas.create_line(559,61,559,596,555,616,539,641,504,656,144,656,112,642,98,623,98,514,width=13,fill="coral")
line_2= cnavas.create_line(790,61,790,220,773,250,734,263,559,263,535,265,520,273,507,299,width=13,fill="DodgerBlue3")
line_3= cnavas.create_line(1011,66,920,66,904,72,897,96,897,268,891,288,866,296,559,296,546,307,542,315,542,431,width=13,fill="skyblue")
line_4=cnavas.create_line(220,306,230,286,244,270,261,263,471,263,486,268,498,277,507,304,513,319,523,328,542,330,749,330,767,335,778,343,790,372,width=13,fill="NavajoWhite3")
line = cnavas.create_line(111,62,111,211,111,233,128,251,143,263,172,266,193,272
                          ,212,288,216,312,216,423,227,445,252,468,283,473
                          ,302,466,328,430,width=13,fill="mediumpurple")

line = cnavas.create_line(329,63,329,263,329,263,329,426,339,450,361,467,
                          394,472,559,472,597,482,613,521,620,563,655,590,
                          658,592,756,592,790,557,790,375,790,352,794,334,815,318,850,318,990,318,1001,310,1009,293,1011,272,width=13,fill="green")

btn = tkinter.Button(frame1, text="검색",command=fn1,width=10,height=3)
btn.place(x=200,y=17)
btn2= tkinter.Button(frame1,text="리셋",command=fn2,width=10,height=3)
btn2.place(x=200,y=77)
    


#1호선=01 2호선=02 3호선=03 4호선=04 동해선=05 부산김해=06
노포=cnavas.create_oval(553,56,565,67,fill="snow",outline="orangered",width=2)
범어사=cnavas.create_oval(553,81,565,92,fill="snow",outline="orangered",width=2)
남산=cnavas.create_oval(553,105,565,116,fill="snow",outline="orangered",width=2)
두실=cnavas.create_oval(553,126,565,137,fill="snow",outline="orangered",width=2)
구서=cnavas.create_oval(553,149,565,160,fill="snow",outline="orangered",width=2)
장전=cnavas.create_oval(553,172,565,183,fill="snow",outline="orangered",width=2)
부산대=cnavas.create_oval(553,195,565,206,fill="snow",outline="orangered",width=2)
온천장=cnavas.create_oval(553,217,565,228,fill="snow",outline="orangered",width=2)
명륜=cnavas.create_oval(553,238,565,249,fill="snow",outline="orangered",width=2)
동래=cnavas.create_oval(551,253,565,276,fill="snow",outline="gray",width=2)
동래_01=cnavas.create_oval(556,258,561,262,fill="coral",outline="orangered",width=2)
동래_04=cnavas.create_oval(556,265,561,269,fill="DodgerBlue3",outline="DodgerBlue3",width=2)
교대=cnavas.create_oval(551,288,565,309,fill="snow",outline="gray",width=2)
교대_01=cnavas.create_oval(556,294,561,298,fill="coral",outline="orangered",width=2)
교대_05=cnavas.create_oval(556,301,561,305,fill="skyblue",outline="skyblue",width=2)
연산=cnavas.create_oval(553,320,565,341,fill="snow",outline="gray",width=2)
연산_03=cnavas.create_oval(558,325,561,329,fill="NavajoWhite3",outline="NavajoWhite2",width=2)
연산_01=cnavas.create_oval(558,331,561,335,fill="snow",outline="orangered",width=2)
시청=cnavas.create_oval(553,360,565,371,fill="snow",outline="orangered",width=2)
양정=cnavas.create_oval(553,397,565,408,fill="snow",outline="orangered",width=2)
부전=cnavas.create_oval(536,427,561,439,fill="snow",outline="gray",width=2)
부전_05=cnavas.create_oval(544,432,548,436,fill="skyblue",outline="skyblue",width=2)
부전_01=cnavas.create_oval(551,432,555,436,fill="coral",outline="orangered",width=2)
서면=cnavas.create_oval(553,460,565,481,fill="snow",outline="gray",width=2)
서면_02=cnavas.create_oval(558,466,561,470,fill="green",outline="green",width=2)
서면_01=cnavas.create_oval(558,473,561,477,fill="coral",outline="orangered",width=2)
범내골=cnavas.create_oval(553,492,565,503,fill="snow",outline="orangered",width=2)
범일=cnavas.create_oval(553,510,565,521,fill="snow",outline="orangered",width=2)
좌천=cnavas.create_oval(553,531,565,542,fill="snow",outline="orangered",width=2)
부산진=cnavas.create_oval(553,552,565,563,fill="snow",outline="orangered",width=2)
초량=cnavas.create_oval(553,572,565,583,fill="snow",outline="orangered",width=2)
부산역=cnavas.create_oval(553,591,565,602,fill="snow",outline="orangered",width=2)
중앙=cnavas.create_oval(548,614,560,625,fill="snow",outline="orangered",width=2)
남포=cnavas.create_oval(532,634,544,645,fill="snow",outline="orangered",width=2)
자갈치=cnavas.create_oval(502,648,514,660,fill="snow",outline="orangered",width=2)
토성=cnavas.create_oval(462,650,474,662,fill="snow",outline="orangered",width=2)
동대신=cnavas.create_oval(423,650,435,662,fill="snow",outline="orangered",width=2)
서대신=cnavas.create_oval(383,650,395,662,fill="snow",outline="orangered",width=2)
대티=cnavas.create_oval(341,650,353,662,fill="snow",outline="orangered",width=2)
괴정=cnavas.create_oval(301,650,313,662,fill="snow",outline="orangered",width=2)
사하=cnavas.create_oval(262,650,274,662,fill="snow",outline="orangered",width=2)
당리=cnavas.create_oval(222,650,234,662,fill="snow",outline="orangered",width=2)
하단=cnavas.create_oval(182,650,194,662,fill="snow",outline="orangered",width=2)
신평=cnavas.create_oval(142,650,154,662,fill="snow",outline="orangered",width=2)
동매=cnavas.create_oval(108,638,120,650,fill="snow",outline="orangered",width=2)
장림=cnavas.create_oval(92,617,104,629,fill="snow",outline="orangered",width=2)
신장림=cnavas.create_oval(92,589,104,601,fill="snow",outline="orangered",width=2)
낫개=cnavas.create_oval(92,563,104,575,fill="snow",outline="orangered",width=2)
다대포항=cnavas.create_oval(92,538,104,550,fill="snow",outline="orangered",width=2)
다대포해수욕장=cnavas.create_oval(92,512,104,524,fill="snow",outline="orangered",width=2)

태화강=cnavas.create_oval(1010,60,1022,72,fill="snow",outline="skyblue",width=2)
개운포=cnavas.create_oval(980,60,992,72,fill="snow",outline="skyblue",width=2)
덕하=cnavas.create_oval(947,60,959,72,fill="snow",outline="skyblue",width=2)
망양=cnavas.create_oval(914,60,926,72,fill="snow",outline="skyblue",width=2)
남창=cnavas.create_oval(891,94,903,106,fill="snow",outline="skyblue",width=2)
서생=cnavas.create_oval(891,115,903,127,fill="snow",outline="skyblue",width=2)
월내=cnavas.create_oval(891,136,903,148,fill="snow",outline="skyblue",width=2)
좌천=cnavas.create_oval(891,158,903,170,fill="snow",outline="skyblue",width=2)
일광=cnavas.create_oval(891,179,903,191,fill="snow",outline="skyblue",width=2)
기장=cnavas.create_oval(891,199,903,211,fill="snow",outline="skyblue",width=2)
오시리아=cnavas.create_oval(891,221,903,233,fill="snow",outline="skyblue",width=2)
송정=cnavas.create_oval(891,242,903,254,fill="snow",outline="skyblue",width=2)
신해운대=cnavas.create_oval(891,263,903,275,fill="snow",outline="skyblue",width=2)
센텀=cnavas.create_oval(825,290,837,302,fill="snow",outline="skyblue",width=2)
재송=cnavas.create_oval(749,290,761,302,fill="snow",outline="skyblue",width=2)
부산원동=cnavas.create_oval(701,290,713,302,fill="snow",outline="skyblue",width=2)
안락=cnavas.create_oval(644,290,656,302,fill="snow",outline="skyblue",width=2)
동래_동해선=cnavas.create_oval(599,290,611,302,fill="snow",outline="skyblue",width=2)
거제=cnavas.create_oval(537,320,548,341,fill="snow",outline="gray",width=2)
거제_03=cnavas.create_oval(540,325,544,329,fill="NavajoWhite3",outline="NavajoWhite2",width=2)
거제_05=cnavas.create_oval(540,331,544,335,fill="skyblue",outline="skyblue",width=2)
거제해맞이=cnavas.create_oval(537,377,549,389,fill="snow",outline="skyblue",width=2)

안평=cnavas.create_oval(784,59,796,71,fill="snow",outline="DodgerBlue3",width=2)
고촌=cnavas.create_oval(784,89,796,101,fill="snow",outline="DodgerBlue3",width=2)
윗반송=cnavas.create_oval(784,124,796,136,fill="snow",outline="DodgerBlue3",width=2)
영산대=cnavas.create_oval(784,156,796,168,fill="snow",outline="DodgerBlue3",width=2)
석대=cnavas.create_oval(784,188,796,200,fill="snow",outline="DodgerBlue3",width=2)
반여농산물시장=cnavas.create_oval(780,219,792,231,fill="snow",outline="DodgerBlue3",width=2)
금사=cnavas.create_oval(763,245,775,257,fill="snow",outline="DodgerBlue3",width=2)
서동=cnavas.create_oval(731,257,743,269,fill="snow",outline="DodgerBlue3",width=2)
명장=cnavas.create_oval(698,257,710,269,fill="snow",outline="DodgerBlue3",width=2)
충렬사=cnavas.create_oval(664,257,676,269,fill="snow",outline="DodgerBlue3",width=2)
낙민=cnavas.create_oval(636,257,649,269,fill="snow",outline="DodgerBlue3",width=2)
수안=cnavas.create_oval(603,257,615,269,fill="snow",outline="DodgerBlue3",width=2)

체육공원=cnavas.create_oval(226,279,238,291,fill="snow",outline="NavajoWhite3",width=2)
강서구청=cnavas.create_oval(257,258,269,270,fill="snow",outline="NavajoWhite3",width=2)
구포=cnavas.create_oval(290,256,302,268,fill="snow",outline="NavajoWhite3",width=2)
숙등=cnavas.create_oval(371,256,383,268,fill="snow",outline="NavajoWhite3",width=2)
남산정=cnavas.create_oval(420,256,432,268,fill="snow",outline="NavajoWhite3",width=2)
만덕=cnavas.create_oval(464,256,476,268,fill="snow",outline="NavajoWhite3",width=2)
미남=cnavas.create_oval(501,288,514,309,fill="snow",outline="gray",width=2)
미남_03=cnavas.create_oval(506,294,510,298,fill="NavajoWhite3",outline="NavajoWhite3",width=2)
미남_04=cnavas.create_oval(506,301,510,305,fill="DodgerBlue3",outline="DodgerBlue3",width=2)
사직=cnavas.create_oval(508,314,520,326,fill="snow",outline="NavajoWhite3",width=2)
종합운동장=cnavas.create_oval(522,322,534,334,fill="snow",outline="NavajoWhite3",width=2)
물만골=cnavas.create_oval(607,324,619,336,fill="snow",outline="NavajoWhite3",width=2)
배산=cnavas.create_oval(671,324,683,336,fill="snow",outline="NavajoWhite3",width=2)
망미=cnavas.create_oval(742,324,754,336,fill="snow",outline="NavajoWhite3",width=2)

# 부산 김해
가야대 = cnavas.create_oval(106,58,117,69, fill="snow",outline="indigo",width=2) # 가야대
장신대 = cnavas.create_oval(106,78,117,89, fill="snow",outline="indigo",width=2)  # 장신대
연지공원 = cnavas.create_oval(106,101,117,112, fill="snow",outline="indigo",width=2)  # 연지공원
박물관 = cnavas.create_oval(106,122,117,133, fill="snow",outline="indigo",width=2)  # 박물관
수로왕릉 = cnavas.create_oval(106,143,117,154, fill="snow",outline="indigo",width=2)  # 수로왕릉
봉황 = cnavas.create_oval(106,165,117,176, fill="snow",outline="indigo",width=2)  # 봉황
부원 = cnavas.create_oval(106,186,117,197, fill="snow",outline="indigo",width=2)  # 부원
김해시청 = cnavas.create_oval(106,208,117,219, fill="snow",outline="indigo",width=2)  # 김해시청
인제대 = cnavas.create_oval(108,231,119,242, fill="snow",outline="indigo",width=2)  # 인제대
김해대학 = cnavas.create_oval(123,247,134,258, fill="snow",outline="indigo",width=2)  # 김해대학
지내 = cnavas.create_oval(143,258,154,269, fill="snow",outline="indigo",width=2)  # 지내
불암 = cnavas.create_oval(165,261,176,272, fill="snow",outline="indigo",width=2)  # 불암
대사 = cnavas.create_oval(186,266,197,278, fill="snow",outline="indigo",width=2)  # 대사
평강 = cnavas.create_oval(203,279,213,290, fill="snow",outline="indigo",width=2)  # 평강

대저 = cnavas.create_oval(209,300,222,321, fill="snow",outline="gray",width=2)  # 대저
대저_01 = cnavas.create_oval(213,304,218,309, fill="indigo",outline="indigo",width=2)
대저_02= cnavas.create_oval(213,312,218,316, fill="NavajoWhite3",outline="NavajoWhite2",width=2)

등구 = cnavas.create_oval(211,350,222,361, fill="snow",outline="indigo",width=2)  # 등구
덕두 = cnavas.create_oval(211,390,222,401, fill="snow",outline="indigo",width=2)  # 덕두
공항 = cnavas.create_oval(220,435,231,446, fill="snow",outline="indigo",width=2)  # 공항
서부산유통지구 = cnavas.create_oval(245,460,256,471, fill="snow",outline="indigo",width=2)  # 서부산 유통지구
괘법르네시떼 = cnavas.create_oval(299,457,310,468, fill="snow",outline="indigo",width=2)  # 괘범 르네시떼



# 부산 2호선

양산 = cnavas.create_oval(323,56,335,67, fill="snow",outline="mediumseagreen",width=2)                  # 양산
남양산 = cnavas.create_oval(323,74,335,86, fill="snow",outline="mediumseagreen",width=2)                # 남양산
부산대양산캠퍼스=cnavas.create_oval(323,95,335,106,fill="snow",outline="mediumseagreen",width=2)        #부산대양산캠퍼스
증산 =cnavas.create_oval(323,114,335,125,fill="snow",outline="mediumseagreen",width=2)       # 증산
호포=cnavas.create_oval(323,133,335,144,fill="snow",outline="mediumseagreen",width=2)        # 호포
금곡=cnavas.create_oval(323,152,335,163,fill="snow",outline="mediumseagreen",width=2)        # 금곡
동원=cnavas.create_oval(323,171,335,182,fill="snow",outline="mediumseagreen",width=2)        # 동원
율리=cnavas.create_oval(323,190,335,201,fill="snow",outline="mediumseagreen",width=2)        # 율리
화명=cnavas.create_oval(323,209,335,220,fill="snow",outline="mediumseagreen",width=2)        # 화명
수정=cnavas.create_oval(323,228,335,239,fill="snow",outline="mediumseagreen",width=2)        # 수정

덕천=cnavas.create_oval(321,248,338,273,fill="snow",outline="gray",width=2)                  # 덕전
덕천_01=cnavas.create_oval(327,255,331,259,fill="NavajoWhite2",outline="NavajoWhite2",width=2)
덕천_04=cnavas.create_oval(327,263,331,267,fill="mediumseagreen",outline="mediumseagreen",width=2)


구명 =cnavas.create_oval(323,288,335,299,fill="snow",outline="mediumseagreen",width=2)      # 구명   
구남 =cnavas.create_oval(323,312,335,323,fill="snow",outline="mediumseagreen",width=2)      # 구남
모라 =cnavas.create_oval(323,336,335,347,fill="snow",outline="mediumseagreen",width=2)      # 모라
모덕 =cnavas.create_oval(323,360,335,371,fill="snow",outline="mediumseagreen",width=2)      # 모덕
덕포 =cnavas.create_oval(323,384,335,395,fill="snow",outline="mediumseagreen",width=2)      # 덕포


사상=cnavas.create_oval(320,412,337,441,fill="snow",outline="gray",width=2)                 # 사상
사상_06=cnavas.create_oval(327,420,331,424,fill="indigo",outline="indigo",width=2)
사상_02=cnavas.create_oval(327,428,331,432,fill="mediumseagreen",outline="mediumseagreen",width=2)
   
감전 =cnavas.create_oval(334,445,345,456,fill="snow",outline="mediumseagreen",width=2)          #  감전
주례 =cnavas.create_oval(358,462,369,473,fill="snow",outline="mediumseagreen",width=2)          #  주례
냉정 =cnavas.create_oval(390,467,401,478,fill="snow",outline="mediumseagreen",width=2)          #  냉정
개금 =cnavas.create_oval(420,467,431,478,fill="snow",outline="mediumseagreen",width=2)          #  개금
동의대 =cnavas.create_oval(451,467,462,478,fill="snow",outline="mediumseagreen",width=2)        #  동의대
가야 =cnavas.create_oval(482,467,493,478,fill="snow",outline="mediumseagreen",width=2)          #  가야
부암 =cnavas.create_oval(515,467,526,478,fill="snow",outline="mediumseagreen",width=2)          #  부암

전포 =cnavas.create_oval(588,476,599,487,fill="snow",outline="mediumseagreen",width=2)                 #전포
국제금융센터_부산은행 =cnavas.create_oval(608,520,619,531,fill="snow",outline="mediumseagreen",width=2)  #국제금융센터_부산은행
문현=cnavas.create_oval(617,561,628,572,fill="snow",outline="mediumseagreen",width=2)  # 문현
지계골=cnavas.create_oval(651,586,662,597,fill="snow",outline="mediumseagreen",width=2)  # 지게골
못골=cnavas.create_oval(697,587,708,598,fill="snow",outline="mediumseagreen",width=2)  # 못골
대연=cnavas.create_oval(747,587,758,598,fill="snow",outline="mediumseagreen",width=2)  # 대연
경성대·부경대=cnavas.create_oval(783,553,794,563,fill="snow",outline="mediumseagreen",width=2)  # 경성대 부경대
남천=cnavas.create_oval(784,500,795,511,fill="snow",outline="mediumseagreen",width=2)  # 남천
금련산=cnavas.create_oval(784,450,795,461,fill="snow",outline="mediumseagreen",width=2)  # 금련사
광안 =cnavas.create_oval(784,400,795,411,fill="snow",outline="mediumseagreen",width=2)  # 광안

수영 =cnavas.create_oval(782,352,798,380,fill="snow",outline="gray",width=2) # 수영
수영_01=cnavas.create_oval(788,360,792,365,fill="skyblue",outline="skyblue",width=2)
수영_02=cnavas.create_oval(788,368,792,373,fill="coral",outline="orangered",width=2)

민락 =cnavas.create_oval(795,322,806,333,fill="snow",outline="mediumseagreen",width=2)           # 민락
센텀시티 =cnavas.create_oval(823,312,834,323,fill="snow",outline="mediumseagreen",width=2)       # 센텀시티


벡스코 =cnavas.create_oval(850,285,868,322,fill="snow",outline="gray",width=2)     # 벡스코(시립미술관)
벡스코_01 =cnavas.create_oval(857,296,862,301,fill="skyblue",outline="skyblue",width=2)
벡스코_02=cnavas.create_oval(857,304,862,309,fill="mediumseagreen",outline="mediumseagreen",width=2)

동백 =cnavas.create_oval(890,312,901,323,fill="snow",outline="mediumseagreen",width=2)  # 동백
해운대 =cnavas.create_oval(940,312,951,323,fill="snow",outline="mediumseagreen",width=2)  # 해운대
중동 =cnavas.create_oval(980,312,991,323,fill="snow",outline="mediumseagreen",width=2)  # 중동
장산 =cnavas.create_oval(1005,270,1016,281,fill="snow",outline="mediumseagreen",width=2)  # 장산

#글씨
#1호선
cnavas.create_text(560,40,text='1호선',font=('궁서체',20),fill="coral")
cnavas.create_text(530,63,text='노포',font=('굴림체',10))
cnavas.create_text(530,87,text='범어사',font=('굴림체',10))
cnavas.create_text(530,110,text='남산',font=('굴림체',10))
cnavas.create_text(530,132,text='두실',font=('굴림체',10))
cnavas.create_text(530,155,text='구서',font=('굴림체',10))
cnavas.create_text(530,178,text='장전',font=('굴림체',10))
cnavas.create_text(530,202,text='부산대',font=('굴림체',10))
cnavas.create_text(530,225,text='온천장',font=('굴림체',10))
cnavas.create_text(530,246,text='명륜',font=('굴림체',10))
cnavas.create_text(580,278,text='동래',font=('굴림체',10))
cnavas.create_text(580,310,text='교대',font=('굴림체',10))
cnavas.create_text(580,345,text='연산',font=('굴림체',10))
cnavas.create_text(580,365,text='시청',font=('굴림체',10))
cnavas.create_text(580,403,text='교대',font=('굴림체',10))
cnavas.create_text(580,435,text='부전',font=('굴림체',10))
cnavas.create_text(580,460,text='서면',font=('굴림체',10))
cnavas.create_text(533,497,text='범내골',font=('굴림체',10))
cnavas.create_text(540,517,text='범일',font=('굴림체',10))
cnavas.create_text(540,538,text='좌천',font=('굴림체',10))
cnavas.create_text(533,559,text='부산진',font=('굴림체',10))
cnavas.create_text(540,578,text='초량',font=('굴림체',10))
cnavas.create_text(533,598,text='부산역',font=('굴림체',10))
cnavas.create_text(532,615,text='중앙',font=('굴림체',10))
cnavas.create_text(522,632,text='남포',font=('굴림체',10))
cnavas.create_text(516,670,text='자갈치',font=('굴림체',10))
cnavas.create_text(470,639,text='토성',font=('굴림체',10))
cnavas.create_text(434,639,text='동대신',font=('굴림체',8))
cnavas.create_text(390,639,text='서대신',font=('굴림체',8))
cnavas.create_text(349,639,text='대티',font=('굴림체',10))
cnavas.create_text(309,639,text='괴정',font=('굴림체',10))
cnavas.create_text(270,639,text='사하',font=('굴림체',10))
cnavas.create_text(230,639,text='당리',font=('굴림체',10))
cnavas.create_text(191,639,text='하단',font=('굴림체',10))
cnavas.create_text(150,639,text='신평',font=('굴림체',10))
cnavas.create_text(110,660,text='동매',font=('굴림체',10))
cnavas.create_text(78,628,text='장림',font=('굴림체',10))
cnavas.create_text(70,598,text='신장림',font=('굴림체',10))
cnavas.create_text(78,570,text='낫개',font=('굴림체',10))
cnavas.create_text(65,545,text='다대포항',font=('굴림체',10))
cnavas.create_text(155,518,text='다대포해수욕장',font=('굴림체',10))
cnavas.create_text(100,495,text='1호선',font=('궁서체',20),fill='coral')

#4호선
cnavas.create_text(790,40,text='4호선',font=('궁서체',20),fill='DodgerBlue3')
cnavas.create_text(812,66,text='안평',font=('굴림체',10))
cnavas.create_text(812,96,text='고촌',font=('굴림체',10))
cnavas.create_text(820,130,text='윗반송',font=('굴림체',10))
cnavas.create_text(820,162,text='영산대',font=('굴림체',10))
cnavas.create_text(812,195,text='석대',font=('굴림체',10))
cnavas.create_text(837,230,text='반여농산물시장',font=('굴림체',8))
cnavas.create_text(780,267,text='금사',font=('굴림체',10))
cnavas.create_text(737,278,text='서동',font=('굴림체',10))
cnavas.create_text(703,278,text='명장',font=('굴림체',10))
cnavas.create_text(673,248,text='충렬사',font=('굴림체',10))
cnavas.create_text(642,278,text='낙민',font=('굴림체',10))
cnavas.create_text(611,248,text='수안',font=('굴림체',10))


#동해선
cnavas.create_text(1062,60,text='동해선',font=('궁서체',20),fill="skyblue")
cnavas.create_text(1020,82,text='태화강',font=('굴림체',10))
cnavas.create_text(986,50,text='개운포',font=('굴림체',10))
cnavas.create_text(955,82,text='덕하',font=('굴림체',10))
cnavas.create_text(923,84,text='망양',font=('굴림체',10))
cnavas.create_text(920,101,text='남창',font=('굴림체',10))
cnavas.create_text(920,122,text='서생',font=('굴림체',10))
cnavas.create_text(920,143,text='월내',font=('굴림체',10))
cnavas.create_text(920,165,text='좌천',font=('굴림체',10))
cnavas.create_text(920,186,text='일광',font=('굴림체',10))
cnavas.create_text(920,207,text='기장',font=('굴림체',10))
cnavas.create_text(932,228,text='오시리아',font=('굴림체',10))
cnavas.create_text(920,249,text='송정',font=('굴림체',10))
cnavas.create_text(932,269,text='신해운대',font=('굴림체',10))
cnavas.create_text(828,280,text='센텀',font=('굴림체',10))
cnavas.create_text(758,310,text='재송',font=('굴림체',10))
cnavas.create_text(710,310,text='부산원동',font=('굴림체',10))
cnavas.create_text(652,310,text='안락',font=('굴림체',10))
cnavas.create_text(610,312,text=' 동래\n동해선',font=('굴림체',8))
cnavas.create_text(500,382,text='거제해맞이',font=('굴림체',10))

# 부산김해선
cnavas.create_text(100,315,text='부산김해' ,font=('궁서체',20),fill='mediumpurple')
cnavas.create_text(113,47,text='가야대' ,font=('굴림체',10))
cnavas.create_text(80,85,text='장신대' ,font=('굴림체',10))
cnavas.create_text(70,105,text='연지공원' ,font=('굴림체',10))
cnavas.create_text(80,128,text='박물관' ,font=('굴림체',10))
cnavas.create_text(70,147,text='수로왕릉' ,font=('굴림체',10))
cnavas.create_text(80,170,text='봉황' ,font=('굴림체',10))
cnavas.create_text(80,190,text='부원' ,font=('굴림체',10))
cnavas.create_text(70,212,text='김해시청' ,font=('굴림체',10))
cnavas.create_text(80,235,text='인제대' ,font=('굴림체',10))
cnavas.create_text(90,260,text='김해대학' ,font=('굴림체',10))
cnavas.create_text(130,280,text='지내' ,font=('굴림체',10))
cnavas.create_text(178,250,text='불암' ,font=('굴림체',10))
cnavas.create_text(213,260,text='대사' ,font=('굴림체',10))
cnavas.create_text(187,293,text='평강' ,font=('굴림체',10))
cnavas.create_text(192,315,text='대저' ,font=('굴림체',10))

cnavas.create_text(192,355,text='등구' ,font=('굴림체',10))
cnavas.create_text(192,400,text='덕두' ,font=('굴림체',10))
cnavas.create_text(192,450,text='공항' ,font=('굴림체',10))
cnavas.create_text(220,490,text=' 서부산\n유통지구' ,font=('굴림체',10))
cnavas.create_text(310,495,text='  괘법\n르네시떼' ,font=('굴림체',10))

# 부산 2호선
cnavas.create_text(980,360,text='2호선',font=('궁서체',20),fill="green")
cnavas.create_text(328,32,text='2호선',font=('궁서체',20),fill="green")
cnavas.create_text(300,62,text='양산',font=('굴림체',10))
cnavas.create_text(300,80,text='남양산',font=('굴림체',10))
cnavas.create_text(380,110,text='부산대\n양산캠퍼스',font=('굴림체',10))
cnavas.create_text(300,120,text='증산',font=('굴림체',10))
cnavas.create_text(300,137,text='호포',font=('굴림체',10))
cnavas.create_text(300,157,text='금곡' ,font=('굴림체',10))
cnavas.create_text(300,176,text='동원',font=('굴림체',10))
cnavas.create_text(300,195,text='율리',font=('굴림체',10))
cnavas.create_text(300,213,text='화명',font=('굴림체',10))
cnavas.create_text(300,233,text='수정',font=('굴림체',10))

cnavas.create_text(355,278,text='덕천',font=('굴림체',10))
cnavas.create_text(300,297,text='구명',font=('굴림체',10))
cnavas.create_text(300,316,text='구남',font=('굴림체',10))
cnavas.create_text(300,339,text='모라',font=('굴림체',10))
cnavas.create_text(300,365,text='모덕',font=('굴림체',10))

cnavas.create_text(300,390,text='덕포',font=('굴림체',10))
cnavas.create_text(355,420,text='사상',font=('굴림체',10))
cnavas.create_text(365,440,text='감전',font=('굴림체',10))
cnavas.create_text(385,455,text='주례',font=('굴림체',10))
cnavas.create_text(395,490,text='냉정',font=('굴림체',10))
cnavas.create_text(428,490,text='개금' ,font=('굴림체',10))

cnavas.create_text(460,455,text='동의대',font=('굴림체',10))
cnavas.create_text(489,490,text='가야',font=('굴림체',10))
cnavas.create_text(525,455,text='부암',font=('굴림체',10))
cnavas.create_text(620,470,text='전포',font=('굴림체',10))

cnavas.create_text(665,520,text='국제금융센터\n  부산은행',font=('굴림체',10))
cnavas.create_text(647,555,text='문현',font=('굴림체',10))
cnavas.create_text(672,573,text='지계골',font=('굴림체',10))
cnavas.create_text(700,610,text='못골',font=('굴림체',10))
cnavas.create_text(760,610,text='대연',font=('굴림체',10))

cnavas.create_text(825,560,text='경성대\n부경대',font=('굴림체',10))
cnavas.create_text(825,505,text='남천',font=('굴림체',10))
cnavas.create_text(825,455,text='금련산',font=('굴림체',10))
cnavas.create_text(818,408,text='광안',font=('굴림체',10))
cnavas.create_text(818,368,text='수영',font=('굴림체',10))
cnavas.create_text(818,347,text='민락',font=('굴림체',10))

cnavas.create_text(860,335,text='센텀시티',font=('굴림체',10))
cnavas.create_text(864,275,text='벡스코',font=('굴림체',10))
cnavas.create_text(899,303,text='동백',font=('굴림체',10))
cnavas.create_text(947,335,text='해운대',font=('굴림체',10))
cnavas.create_text(995,335,text='중동',font=('굴림체',10))
cnavas.create_text(1010,260,text='장산',font=('굴림체',10))

# 부산 3호선 라벨
cnavas.create_text(420,220,text='3호선',font=('궁서체',20),fill='NavajoWhite3')
cnavas.create_text(253,305,text='체육\n공원',font=('굴림체',10))
cnavas.create_text(257,240,text='강서\n구청',font=('굴림체',10))
cnavas.create_text(295,278,text='구포',font=('굴림체',10))
cnavas.create_text(376,246,text='숙등',font=('굴림체',10))
cnavas.create_text(425,246,text='남산정',font=('굴림체',10))
cnavas.create_text(470,246,text='만덕',font=('굴림체',10))
cnavas.create_text(480,300,text='미남',font=('굴림체',10))
cnavas.create_text(490,320,text='사직',font=('굴림체',10))
cnavas.create_text(490,340,text='종합운동장',font=('굴림체',10))
cnavas.create_text(613,347,text='물만골',font=('굴림체',10))
cnavas.create_text(678,347,text='배산',font=('굴림체',10))
cnavas.create_text(745,347,text='망미',font=('굴림체',10))




window.mainloop()