import tkinter
window=tkinter.Tk()
window.geometry("200x250")

su=0
def num(st):
    input1.insert(100,st)

def re():
    global su
    input1.delete(0,10000)
    su=0
    
def calc():
    global su
    su=eval(input1.get())
    input1.delete(0,10000)
    input1.insert(100,su)
    su=0


input1=tkinter.Entry(window)
input1.pack()

b1=tkinter.Button(window,text="%",width=5,height=3,command=lambda:num('%'))
b1.place(x=10,y=25)
b2=tkinter.Button(window,text="*",width=5,height=3,command=lambda:num('*'))
b2.place(x=55,y=25)
b3=tkinter.Button(window,text="/",width=5,height=3,command=lambda:num('/'))
b3.place(x=100,y=25)
b4=tkinter.Button(window,text="C",width=5,height=3,command=re)
b4.place(x=145,y=25)
b5=tkinter.Button(window,text="7",width=5,height=3,command=lambda:num('7'))
b5.place(x=10,y=80)
b6=tkinter.Button(window,text="8",width=5,height=3,command=lambda:num('8'))
b6.place(x=55,y=80)
b7=tkinter.Button(window,text="9",width=5,height=3,command=lambda:num('9'))
b7.place(x=100,y=80)
b8=tkinter.Button(window,text="+",width=5,height=3,command=lambda:num('+'))
b8.place(x=145,y=80)
b9=tkinter.Button(window,text="4",width=5,height=3,command=lambda:num('4'))
b9.place(x=10,y=135)
b10=tkinter.Button(window,text="5",width=5,height=3,command=lambda:num('5'))
b10.place(x=55,y=135)
b11=tkinter.Button(window,text="6",width=5,height=3,command=lambda:num('6'))
b11.place(x=100,y=135)
b12=tkinter.Button(window,text="-",width=5,height=3,command=lambda:num('-'))
b12.place(x=145,y=135)
b13=tkinter.Button(window,text="1",width=5,height=3,command=lambda:num('1'))
b13.place(x=10,y=190)
b14=tkinter.Button(window,text="2",width=5,height=3,command=lambda:num('2'))
b14.place(x=55,y=190)
b15=tkinter.Button(window,text="3",width=5,height=3,command=lambda:num('3'))
b15.place(x=100,y=190)
b16=tkinter.Button(window,text="=",width=5,height=3,command=calc)
b16.place(x=145,y=190)



window.mainloop()