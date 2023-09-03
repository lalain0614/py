import tkinter
window=tkinter.Tk()
window.geometry("650x400")

def check():
    label.config(text="rdvar_1 = "+str(rdvar_1.get())+"\n" + 
                "rdvar 2= "+str(rdvar_2.get())+"\n" + 
                "total = "+str(rdvar_2.get()+rdvar_2.get()))
                    

rdvar_1=tkinter.IntVar()
rdvar_2=tkinter.IntVar()
radio1=tkinter.Radiobutton(window,text="1",variable=rdvar_1,value=3,command=check)
radio1.pack()
radio2=tkinter.Radiobutton(window,text="2",variable=rdvar_1,value=3,command=check)
radio2.pack()
radio3=tkinter.Radiobutton(window,text="3",variable=rdvar_1,value=9,command=check)
radio3.pack()

radio4=tkinter.Radiobutton(window,text="4",variable=rdvar_2,value=18,command=check)
radio4.pack()
radio5=tkinter.Radiobutton(window,text="5",variable=rdvar_2,value=28,command=check)
radio5.pack()

label=tkinter.Label(window,text="none",height=7)
label.pack()

window.mainloop()

