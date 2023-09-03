import tkinter

window= tkinter.Tk()
window.geometry("300x300")

a=tkinter.IntVar()
b=tkinter.IntVar()
c=tkinter.IntVar()

chk_btn1=tkinter.Checkbutton(window, text="a", variable=a)
chk_btn2=tkinter.Checkbutton(window, text="b", variable=b)
chk_btn3=tkinter.Checkbutton(window, text="c", variable=c)

chk_btn1.pack()
chk_btn2.pack()
chk_btn3.pack()

window.mainloop()