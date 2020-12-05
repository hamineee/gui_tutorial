from tkinter import *

root = Tk()
root.title("Hello GUI")
root.geometry("640x480+300+100")

btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, padx=20, pady=5, text="button2-----------")
btn2.pack()

btn3 = Button(root, padx=5, pady=20, text="button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button4-----------")
btn4.pack()

btn5 = Button(root, fg="blue", bg="black", text="button5")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("You just clicked a Button !")

btn7 = Button(root, text="Click ME!", command=btncmd)
btn7.pack()

root.mainloop() #mainloop > 창이 닫히지 않도록 해준다 