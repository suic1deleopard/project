from tkinter import *
import tkinter 
from components.function import Function
from components.interface_for_function import Interface_for_function
def Plus:
def Minus:
    
class Buttom_create:
    def __init__(self, context:tkinter.Canvas):
        self.c = context
    def b(self):
        Button1 = tkinter.Button(self.c, width=1,   text='+', command= Plus, activebackground= 'orange')
        Button1.pack()
        Button2 = tkinter.Button(self.c, width=1, text='-', command= Minus, activebackground= 'orange')
        Button2.pack()
        self.c.create_window((55, 105), anchor="nw", window=Button1)
        self.c.create_window((80, 105), anchor="nw", window=Button2)
