import tkinter
window = tkinter.Tk()
window.geometry("650x470")

def calc(event):
    label.config(text="결과 = "+str(eval(entry.get())))
    entry.delete(0,10)

entry=tkinter.Entry(window)
entry.bind("<Return>",calc)#event(key,mouse) <button-1>=>왼쪽버튼
entry.pack()#pack(위치,라인이 기준,l/r/t/b)
entry.insert(0,"식을 입력하세요")

label=tkinter.Label(window,text="결과")
label.pack()

window.mainloop()
"""pack은 같은 라인에 두개가 나올 수 없음
grid 격자 위치(0,0~x,y)
place 좌표(컴퓨터의 픽셀단위)

"""
"""entry 기능
insert(인덱스,"문자열")=인덱스의 위치에 문자열을 추가
delete(start_index,end_index)=start~end문자열 삭제
get()=입력된 내용 가져오기
select_____=블록처리(범위선택)
insertwidth=키보드 커서 두께
insertbackground=키보드 커서 색상
"""