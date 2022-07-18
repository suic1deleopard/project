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
q.palka()
f.plus()
def Plus():
    f.plus()
Button1 = tkinter.Button(root, width=3,   text='+', command= Plus, activebackground= 'silver')
Button1.pack()
ca.create_window((60, 105), anchor="nw", window=Button1)
root.mainloop()
