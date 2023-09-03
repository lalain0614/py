import tkinter
import tkinter.font
tk= tkinter.Tk()
tk.geometry("500x330+100+100")
tk.resizable(False,False)
font=tkinter.font.Font(family="궁서체",size=15)
lb=tkinter.Label(tk, text="안녕하세요",width=10,height=5,foreground="red",relief="sunken",background="gray",borderwidth=5,font=font)
lb.pack()
str_var=tkinter.StringVar()
str_var.set("반갑습니다.")
label=tkinter.Label(tk,textvariable=str_var,width=20,height=10,relief="solid",bd=5,anchor="ne")
label.pack()
tk.mainloop()



"""label 기능
text= 입력기능 // textvariavle= 가져올 변수 (문자열)
anchor=내용의 이미지 위치_e,w,s,n,ne,es,nw,sw,center
justify=정렬_left,right,center
width=너비/height=높이
relief=테두리 모양_flat,greove,raised,suken,solid(선)
borderwidth=bd=테두리 굵기
background=bg=배경색
foreground=fg=문자열색
"""