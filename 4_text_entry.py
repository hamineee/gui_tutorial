from tkinter import *

root = Tk()
root.title("hello GUI")
root.geometry("500x500+300+100")

txt = Text(root, width=30, height=5) #Enter 가능, 여러줄로 정보를 입력받을 때 사용
txt.pack()

txt.insert(END, "Type Something!")

e = Entry(root, width=30) #Enter 불가능, 한줄로 정보를 입력받을 때 사용
e.pack()
e.insert(0, "Write something, in only one line")

def btncmd():
    # 내용출력
    print(txt.get("1.0", END)) # 1: line1부터 가져와라 / 0: column기준으로 0번째 위치(index)에서 부터 가져와라 / END: 끝까지 가져와라
    print(e.get())
    # 내용삭제
    txt.delete("1.0", END) 
    e.delete(0, END)
btn = Button(root, text="Click!", command=btncmd)
btn.pack()

root.mainloop()