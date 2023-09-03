import tkinter

window=tkinter.Tk()
window.geometry("650x400")

b1=tkinter.Button(window, text='(50,50)')
b2=tkinter.Button(window, text='(50,100)')
b3=tkinter.Button(window, text='(10,10)')
b4=tkinter.Button(window, text='(0,200)')
b5=tkinter.Button(window, text='(50,300)1')
b6=tkinter.Button(window, text='(50,300)2')

b1.place(x=0,y=0,relx=0.1)
b2.place(x=0,y=0,)
b3.place(x=50,y=50)
b4.place(x=0,y=200)
b5.place(x=50,y=300)
b6.place(x=50,y=300,relx=0.1)
window.mainloop()