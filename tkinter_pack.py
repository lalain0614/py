import tkinter

window=tkinter.Tk()
window.geometry("650x400")

l1=tkinter.Label(window, text="top-1")
l2=tkinter.Label(window,text="top-2")
l1.pack(side="top")
l2.pack(side="top")

b1=tkinter.Button(window,text="left-1")
b2=tkinter.Button(window,text="left-2")
b3=tkinter.Button(window,text="left-3")
b4=tkinter.Button(window,text="left-4")
b1.pack(side="left")
b2.pack(side="left",fill="y")
b3.pack(side="bottom",anchor="e")
b4.pack(side="bottom")
b5=tkinter.Button(window,text="center")
b5.pack(expand=True,fill="both")
window.mainloop()