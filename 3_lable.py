from tkinter import *

root = Tk()
root.title("Hello GUI")
root.geometry("500x500+300+100")

#label은 텍스트나 이미지를 그냥 보여주는 것, 클릭해도 어떤 반응을 하지는 않는다.

label1 = Label(root, text="Hello World")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="Bye World", fg="blue")

    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="click!", command=change)
btn.pack()

root.mainloop()
