import tkinter
from PIL import ImageTk,Image
window=tkinter.Tk()
window.geometry("1000x650")

image=Image.open("note02_01.jpg")
img=ImageTk.PhotoImage(image)
label=tkinter.Label(window,image=img)
label.pack()

window.mainloop()

