import tkinter

window=tkinter.Tk()
window.title("button 연습")
window.geometry("300x150+1100+400")
cnt=0
def cntup():
    global cnt
    cnt+=1
    label.config(text="{0:+,}".format(cnt))
def cntdn():
    global cnt
    cnt-=1
    if cnt<1:
        cnt=0
    label.config(text="{0:+,}".format(cnt))

label=tkinter.Label(window,text="{0:+,}".format(cnt))
label.pack()
button=tkinter.Button(window,text="버튼up",width=10,overrelief="solid",command=cntup,repeatdelay=1000,repeatinterval=100)
button.pack()
button2=tkinter.Button(window,text="버튼down",width=10,overrelief="solid",command=cntdn,repeatdelay=1000,repeatinterval=100)
button2.pack()

window.mainloop()

"""
relief=버튼의 기본 모양//overrelief=마우스를 올렸을 때 모양
state=상태설정_nomal,active,disavled
activebackground=active상태일 떄 배경색
activeforeground=active 상태일 때 글자색
disavledforegroune=disavled상태일 때 글자색
highlightcolor=버튼이 선택되었을 때 색상
highlightbackground=버튼이 선택되지 않았을 때 색상
takefocuss=tab키를 눌렀을 때 이동허용 여부
command=active 상태일 때 실행하는 함수(매서드)
repeatdelay=버튼이 눌러진 상태에서 command 실행까지의 대기시간(밀리초)
repeatinterval=버튼이 눌러진 상태에서 command 실행 반복시간(밀리초)
"""