from tkinter import *
root = Tk()
root.title('Баночный барометр')
c = Canvas(root, width=500,height=450,background = "white")
c.create_rectangle(50,50,100,100, fill = 'lightgray')
c.create_rectangle(60,70,90,95, fill = 'lightgray')
c.create_text(75,60,text= 'Дата', font= 'Times 12')
c.create_rectangle(240,50,310,100, fill = 'lightgray')
c.create_rectangle(260,70,290,95, fill = 'lightgray')
c.create_text(275,60,text= 'Значение', font= 'Times 12')
c.create_oval(102, 150, 298,240, 
            fill = '#e6fefe', outline= '#e6fefe')
c.create_arc(102, 150, 298,240,
             start = 180 , extent = 180, width = 4 , style = ARC, outline = 'pink')
c.create_line(100, 400, 100,175)
c.create_line(300, 400, 300,175)
c.create_arc(100, 375, 300,425 ,
             start=180, extent=180, style=ARC,width=1.25)
c.create_arc(102, 375, 298,425 , 
            start=180, extent=-180, style=ARC,width=1.25, outline = 'gray', dash=(4, 2))
c.create_oval(100, 130, 300,225 ,
             fill = '#e6fefe')
c.create_rectangle(320,130,400,250, fill = 'lightgrey')
c.create_text(385,150, text="800", font='Times 10')
c.create_text(385,175, text="750", font='Times 10')
c.create_text(385,200, text="700", font='Times 10')
c.create_text(385,225, text="650", font='Times 10')
c.create_line(330,150,370,150, width= 2)
y = 155
i  = 0
q = 0
while i < 16:
    if q == 25:
        c.create_line(330,y,370,y, width= 2) 
        q = 0      
    c.create_line(335,y,365,y, width= 1)
    i += 1
    y+= 5
    q+= 5 
c.create_polygon((200, 175), (350, 175), 
                (350 ,185 ), (200, 185), 
                fill='#ffe493', outline='black')
c.create_line(200,150,245,200, width= 5, fill = 'pink')
c.pack()
mainloop()  