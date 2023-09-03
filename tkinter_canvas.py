""" 
line//polygon//oval//arc//imige
"""
import tkinter
window=tkinter.Tk()
window.geometry("650x400")

canvas=tkinter.Canvas(window,relief="solid",bd=3)

line= canvas.create_line(10,10,50,50,0,100,width=5,fill="red")

polygon=canvas.create_polygon(50,50,150,150,50,150,150,50)
polygon2=canvas.create_polygon(150,150,250,150,250,250,150,250)
oval=canvas.create_oval(200,50,400,250,outline="red",fill="blue")
arc=canvas.create_arc(100,100,300,300,start=150,extent=150,fill="gray")


canvas.pack()
window.mainloop()