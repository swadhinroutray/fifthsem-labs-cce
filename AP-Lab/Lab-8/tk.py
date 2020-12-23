import tkinter
from tkinter import * 

gui = Tk()

b1 = Button(gui,text = "Hello there", command= sys.exit) 
b1.pack()
mainloop()