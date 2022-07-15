import tkinter
from components.interface import Interface
from tkinter import *
root = Tk()
root.title('Баночный барометр')
ca = Canvas(root, width=500,height=450,background = "white")
i = Interface(ca)
b = Button(ca)
i.create()
root.mainloop()
