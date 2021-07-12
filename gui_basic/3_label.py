import os
from tkinter import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()

root.title('Basic GUI')
root.geometry('640x480')

label1 = Label(root, text='안녕하세요')
label1.pack()

photo = PhotoImage(file=resource_path('gui_basic/img.png'))
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='또 만나요')

    global photo2 # 함수 내에서 레이블의 이미지를 바꾸기 위해 전역 변수 선언
    photo2 = PhotoImage(file=resource_path('gui_basic/img2.png'))
    label2.config(image=photo2)

btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop()