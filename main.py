import tkinter
import webbrowser
from components.interface import Interface
from components.function import Function
from components.interface_for_function import Interface_for_function
from tkinter import *
root = Tk()
root.title('Баночный барометр')
root.configure(width=504,height=454,background = "#f5efe1")
l = 1
ca = Canvas(root, width=500,height=450,background = "#f5efe1")
i = Interface(ca)
f = Function(ca)
q = Interface_for_function(ca)
def Close():
    root.destroy()
def callback(event):
    webbrowser.open("https://github.com/suic1deleopard/project")
def Begin():
    Button4.place(x = 20, y = 15)
    Button3.destroy()
    i.create()
    q.palka()
    f.plus()
    Button1 = tkinter.Button(root, width=3,   text='+', command= Plus, activebackground= 'silver', cursor="hand2")
    Button1.pack()
    ca.create_window((60, 105), anchor="nw", window=Button1)
def Back():
    Button3 = tkinter.Button(root, width=50,   text='Завершить лабораторную работу', command= Close, activebackground= 'silver',
    cursor="hand2",)
    Button3.place(x = 75, y = 180)
    Button4.destroy()
    ca.delete('all')
    i.k()
Button3 = tkinter.Button(root, width=50,   text='Начать выполнение лабораторной работы', command= Begin, activebackground= 'silver',
cursor="hand2",)
Button3.place(x = 75, y = 180)
Button4 = tkinter.Button(root, width=10,   text='Закончить', command= Back, activebackground= 'silver',
cursor="hand2", bg = '#f5efe1')
label = tkinter.Label(root, text="Проект на GitHub", bg = '#f5efe1', cursor="hand2")
label.pack()
label.place( x = 20, y = 420)
label.bind("<Button-1>", callback)
def Plus():
    f.plus()
root.mainloop()
