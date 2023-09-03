import tkinter

window=tkinter.Tk()

window.geometry("600x300")

listbox= tkinter.Listbox(window,selectmode="single",height=0)#extended 컨트롤 누르거나 드래그로 다중선택가능
listbox.insert(0,"한국")
listbox.insert(1,"일본")
listbox.insert(3,"미국")
listbox.insert(2,"중국")

listbox.pack()
def btnclick():
    print("선택 된 것 : ",listbox.get(listbox.curselection()))
btn=tkinter.Button(window,text="클릭",command=btnclick)
btn.pack()
window.mainloop()