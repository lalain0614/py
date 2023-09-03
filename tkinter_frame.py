import tkinter
window=tkinter.Tk()
window.geometry('1000x650')

frame3=tkinter.Frame(window,relief="solid",bd=3,height=200)
frame3.pack(side="top",fill="x")

frame1=tkinter.Frame(window,relief="solid",bd=3)
frame1.pack(side="left",fill="both",expand=True)
frame2=tkinter.Frame(window,relief="solid",bd=3)
frame2.pack(side="right",fill="both",expand=True)

label1=tkinter.Label(frame3,text="top")
label2=tkinter.Label(frame1,text="left")
label3=tkinter.Label(frame2,text="right")
label1.pack(side="right")
label2.pack(side="left")
label3.pack(side="bottom",anchor="e")
window.mainloop()