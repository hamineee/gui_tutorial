from tkinter import *

root = Tk()
root.title("Hello GUI")
root.geometry("500x500+300+100")

listbox = Listbox(root, selectmode="extended", height=3)
#selectmode: single= 아이템 하나만 선택가능 / extended= 아이템 여러개 선택가능
#height= 0이면 item 전체 다 보여줌 / 다른 숫자 입력시 입력한 숫자 개수만큼만 보여줌, 다 안보일 시 보통 스크롤 바 나옴
listbox.insert(0, 'Apple')
listbox.insert(1, 'Strawberry')
listbox.insert(2, 'Banana')
listbox.insert(END, 'Watermelon')
listbox.insert(END, 'Grape')
listbox.pack()

def btncmd():
    # 삭제
    #listbox.delete(1) #1: 2번째 아이템 삭제 / END: 마지막 아이템 삭제

    # 개수확인
    #print(listbox.size(),"items are in the list")

    # 항목확인
    print("list 1 to 3:", listbox.get(0,2)) #listbox.get(시작index, 끝index)

    # 선택된 항목확인 (index로 반환)
    print("selected items:", listbox.curselection())

 
btn = Button(text="Click!", command=btncmd)
btn.pack()

root.mainloop()