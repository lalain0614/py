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

cnavas=tkinter.Canvas(frame2,relief="solid",bd=3,width=1100,height=800)
cnavas.pack(fill="both")

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
    if start=='노포':
       cnavas.itemconfig(노포,fill="blue")
    elif start=='범어사':
       cnavas.itemconfig(범어사,fill='blue')
    elif start=='남산':
       cnavas.itemconfig(남산,fill="blue")
    
    if end=='노포':
        cnavas.itemconfig(노포,fill='red')
    elif end=='범어사':
        cnavas.itemconfig(범어사,fill='red')    
        
def fn2():
    global start
    global end
    start=input1.get()
    end=input2.get()
    if start=='노포':
       cnavas.itemconfig(노포,fill="snow")
    elif start=='범어사':
       cnavas.itemconfig(범어사,fill='snow')
    elif start=='남산':
       cnavas.itemconfig(남산,fill="snow")
    if end=='노포':
        cnavas.itemconfig(노포,fill='snow')
    elif end=='범어사':
        cnavas.itemconfig(범어사,fill='snow')    
        
    
    input1.delete(0,10000)
    input2.delete(0,10000)
    i=''

"""def fn1():
    b1=cnavas.create_oval(553,126,565,137,fill="red",outline="orangered",width=2)     
    line_2= cnavas.create_line(553,126,565,137,553,172,565,183,width=10,fill="black")
    b2=cnavas.create_oval(553,172,565,183,fill="red",outline="orangered",width=2)     """


line_1= cnavas.create_line(559,61,559,596,555,616,539,641,504,656,144,656,112,642,98,623,98,514,width=7,fill="coral")
line_2= cnavas.create_line(790,61,790,220,773,250,734,263,559,263,535,265,520,273,507,299,width=7,fill="DodgerBlue3")
line_3= cnavas.create_line(1011,66,920,66,904,72,897,96,897,268,891,288,866,296,559,296,546,307,542,315,542,431,width=7,fill="skyblue")
line_4=cnavas.create_line(220,306,230,286,244,270,261,263,471,263,486,268,498,277,507,304,513,319,523,328,542,330,749,330,767,335,778,343,790,372,width=7,fill="NavajoWhite3")


    
btn = tkinter.Button(frame1, text="색을 바꿔",command=fn1,width=10,height=3)
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
동래=cnavas.create_oval(553,253,565,274,fill="snow",outline="gray",width=2)
동래_01=cnavas.create_oval(558,258,561,262,fill="coral",outline="orangered",width=2)
동래_04=cnavas.create_oval(558,265,561,269,fill="DodgerBlue3",outline="DodgerBlue3",width=2)
교대=cnavas.create_oval(553,288,565,309,fill="snow",outline="gray",width=2)
교대_01=cnavas.create_oval(558,294,561,298,fill="coral",outline="orangered",width=2)
교대_05=cnavas.create_oval(558,301,561,305,fill="skyblue",outline="skyblue",width=2)
연산=cnavas.create_oval(553,320,565,341,fill="snow",outline="gray",width=2)
연산_03=cnavas.create_oval(558,325,561,329,fill="NavajoWhite3",outline="NavajoWhite2",width=2)
연산_01=cnavas.create_oval(558,331,561,335,fill="snow",outline="orangered",width=2)
시청=cnavas.create_oval(553,360,565,371,fill="snow",outline="orangered",width=2)
양정=cnavas.create_oval(553,397,565,408,fill="snow",outline="orangered",width=2)
부전=cnavas.create_oval(538,429,561,439,fill="snow",outline="gray",width=2)
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
도성=cnavas.create_oval(462,650,474,662,fill="snow",outline="orangered",width=2)
동대신=cnavas.create_oval(423,650,435,662,fill="snow",outline="orangered",width=2)
서대신=cnavas.create_oval(383,650,395,662,fill="snow",outline="orangered",width=2)
대티=cnavas.create_oval(341,650,353,662,fill="snow",outline="orangered",width=2)
과정=cnavas.create_oval(301,650,313,662,fill="snow",outline="orangered",width=2)
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




window.mainloop()