from tkinter import *
import tkinter 
from random import *
import random
class Function:
    def __init__(self, context:tkinter.Canvas):
        self.c = context
        self.date = 0
        self.a = 0
        self.b = 175
        self.q = 0
    def function(self):
        self.a = randint(740,800)
        self.q = (self.a - 740) / 2
        self.c.delete('a')
        self.c.delete('b')
        self.c.create_rectangle(60,70,90,95, fill = '#eaeaea')
        self.c.create_text(75,82, text=self.date, font= 'Times 12')
        self.c.create_rectangle(260,70,290,95, fill = '#eaeaea')
        self.c.create_text(275,82, text=self.a, font= 'Times 12')
        self.c.create_polygon((200, (175 - self.q )), (350, (175 -self.q )), (350 ,(185 -self.q )),
        (200, (185 -self.q )), fill='#f0e8d2', outline='black', tag = 'a')
        self.c.create_line(200,160 - self.q,245,200 - self.q, width= 5, fill = '#ababab', tag = 'b')
    def plus(self):
        if self.date < 14:
            self.date += 1
            self.function()
