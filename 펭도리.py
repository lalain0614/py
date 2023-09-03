import tkinter
window=tkinter.Tk()
window.geometry("650x400")

cnavas=tkinter.Canvas(window,relief="solid",bd=3)

oval=cnavas.create_oval(95,100,200,205,fill="DodgerBlue3",outline="DodgerBlue3")
polygon=cnavas.create_polygon(138,150,140,150,140,140)
polygon2=cnavas.create_polygon(160,150,150,150,155,140)


oval=cnavas.create_oval(95,130,140,185,fill="snow",outline="snow")
oval=cnavas.create_oval(155,130,200,185,fill="snow",outline="snow")
arc=cnavas.create_arc(98,140,198,205,start=0,extent=-180,fill="snow",outline="snow")
oval=cnavas.create_oval(170,150,180,180,fill="blue")
oval=cnavas.create_oval(115,150,125,180,fill="blue")
oval=cnavas.create_oval(117,155,123,175,fill="black")
oval=cnavas.create_oval(172,155,178,175,fill="black")
oval=cnavas.create_oval(117,160,123,150,fill="snow")
oval=cnavas.create_oval(172,160,178,150,fill="snow")
oval=cnavas.create_oval(135,165,160,180,fill="LightGoldenrod1",outline="LightGoldenrod1")
line=cnavas.create_line(137,175,160,175,fill="gray")

cnavas.pack()
window.mainloop()