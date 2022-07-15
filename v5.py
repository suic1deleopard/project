import tkinter
from components.interface import Interface
from components.function import Function
from components.interface_for_function import Interface_for_function
from tkinter import *
root = Tk()
root.title('Баночный барометр')
ca = Canvas(root, width=500,height=450,background = "#f5efe1")
i = Interface(ca)
f = Function(ca)
q = Interface_for_function(ca)
i.create()
def Plus():
    q.create1()
    f.plus()
def Minus():
    q.create1()
    f.minus()
Button1 = tkinter.Button(root, width=1,   text='+', command= Plus, activebackground= 'orange')
Button1.pack()
Button2 = tkinter.Button(root, width=1, text='-', command= Minus, activebackground= 'orange')
Button2.pack()
ca.create_window((55, 105), anchor="nw", window=Button1)
ca.create_window((80, 105), anchor="nw", window=Button2)
root.mainloop()
