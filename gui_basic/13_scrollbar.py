from tkinter import *

root = Tk()
root.title('Basic GUI')
root.geometry('640x480+300+100') # 크기 지정, x좌표, y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set) # 참고1
for i in range(1, 32):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview) # 참고2

# 참고1(scrollbar.set)과 참고2 세팅이 되어야 스크롤바와 리스트박스가 상호작용됨

root.mainloop()