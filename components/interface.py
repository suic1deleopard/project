from tkinter import *
import tkinter 
class Interface:
    def __init__(self, context:tkinter.Canvas):
        self.c = context
    
    def create(self):
        self.banka()
        self.tablo1()
        self.skala()
        self.tablo2()
        self.pole_l()
        self.pole_r()
        self.c.pack()


    def banka(self):
        self.c.create_rectangle(100,175,300,400, fill= '#eaeaea')
        self.c.create_oval(102, 150, 298,240, 
            fill = '#ebfefe', outline= '#ebfefe')
        self.c.create_arc(102, 150, 298,240,
             start = 180 , extent = 180, width = 4 , style = ARC, outline = '#ababab')
    
        self.c.create_oval(100, 375, 300,425 , fill= '#eaeaea')
        self.c.create_arc(102, 375, 298,425 , 
            start=180, extent=-180, style=ARC,width=3, outline = '#eaeaea')
        self.c.create_arc(102, 375, 298,425 , 
            start=180, extent=-180, style=ARC, outline = 'black', dash=(4, 2))
        self.c.create_oval(100, 130, 300,225 ,
             fill = '#e6fefe')
    
    def tablo1(self):
        self.c.create_rectangle(50,50,100,100, fill = '#eaeaea')
        self.c.create_rectangle(60,70,90,95, fill = '#eaeaea')
        self.c.create_text(75,60,text= 'Дата', font= 'Times 12')
        self.c.create_text(60,70, text=1)
    def tablo2(self):
        self.c.create_rectangle(240,50,310,100, fill = '#eaeaea')
        self.c.create_rectangle(260,70,290,95, fill = '#eaeaea')
        self.c.create_text(275,60,text= 'Значение', font= 'Times 12')

    def skala(self):
        self.c.create_rectangle(330,130,410,250, fill = '#eaeaea')
        self.c.create_text(395,150, text="800", font='Times 10')
        self.c.create_text(395,175, text="750", font='Times 10')
        self.c.create_text(395,200, text="700", font='Times 10')
        self.c.create_text(395,225, text="650", font='Times 10')
        self.c.create_line(340,150,380,150, width= 2)
        y = 150
        i  = 0
        q = 0
        while i < 16:
            if q == 25:
                self.c.create_line(340,y,380,y, width= 2) 
                q = 0      
            self.c.create_line(345,y,375,y, width= 1)
            i += 1
            y+= 5
            q+= 5 
    def pole_l(self):
        self.c.create_text(405,270,text= 'Результаты измерений', font= 'Times 10')
        x = 320
        y = 300
        z = 1
        for i in range(7):
            text1 = Entry(self.c, width = 10, bg='#eaeaea')
            self.c.create_text(x,y,text= z, font= 'Times 11')
            text1.place(x = (x+10), y = (y-10))
            y += 20
            z += 2
    def pole_r(self):
            x = 405
            y = 300
            z = 2
            for i in range(7):
                text1 = Entry(self.c, width = 10, bg='#eaeaea')
                self.c.create_text(x,y,text= z, font= 'Times 11')
                text1.place(x = (x+10), y = (y-10))
                y += 20
                z += 2