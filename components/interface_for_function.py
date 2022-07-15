from tkinter import *
import tkinter 
class Interface_for_function:
    def __init__(self, context:tkinter.Canvas):
        self.c = context  
    def palka(self):
        self.c.create_polygon((200, 175), (350, 175), 
                (350 ,185 ), (200, 185), 
                fill='#ffe493', outline='black', tag = 'a')
        self.c.create_line(200,160,245,200, width= 5, fill = 'pink', tag = 'b')
    def palka_remove(self):
        self.c.delete('a')
        self.c.delete('b')