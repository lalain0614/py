import tkinter

window=tkinter.Tk()
window.geometry("650x400")

b1=tkinter.Button(window,text="(0,0)")
b2=tkinter.Button(window,text="(0,1)",width=20)
b3=tkinter.Button(window,text="(0,2)")
b4=tkinter.Button(window,text="(1,0)",height=20)
b5=tkinter.Button(window,text="(1,1)")
b6=tkinter.Button(window,text="(1,2)")
b7=tkinter.Button(window,text="(3,3)")
b8=tkinter.Button(window,text="(2,2)")
b9=tkinter.Button(window,text="(2,0)")

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0,rowspan=3)
b5.grid(row=1,column=1,sticky="w")
b6.grid(row=1,column=2)
b7.grid(row=3,column=3)
b8.grid(row=2,column=2)
b8.grid(row=2,column=0)

window.mainloop()