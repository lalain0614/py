import tkinter

window=tkinter.Tk()
window.geometry("600x400+300+150") #넓이*높이+가로위치+세로위치
window.resizable(False,False)#넓이 고정
window.title("tk inter")#타이틀 바꾸기
label =tkinter.Label(window, text="hello tk~")
label.pack()#텍스트 넣기, pack은 하나만 나옴
label2=tkinter.Label(window, text="bye~")
label2.pack()

window.mainloop()
