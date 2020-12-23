import tkinter
from tkinter import *
import tkMessageBox

import sqlite3

def addPerson():
    print("hello")
    print(name.get("1.0",END))
    f = open('LogBook.txt','a')
    c.execute("Insert into DETAILS values(?,?);",(name.get("1.0",END),int(phone.get("1.0",END))))
    data = c.execute("Select * from DETAILS")
    for i in data: 
        print(i[0])
        f.write(i[0] +'\n')



    def alertBox():
        tkMessageBox.showinfo("Clicked here")


conn = sqlite3.connect("darshilOP.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS DETAILS(
    name varchar(30) primary key,
    phone int(10) 
)''')
c.execute("Insert into DETAILS values('Hello',123);")
x = (c.execute("Select * from DETAILS"))
for i in x:
    print(i)
gui = Tk()

gui.geometry("400x400")

count_label = Text(gui,width=10,height=10)
name_label= Label(gui,text="Name")
phone_label = Label(gui, text="Phone")
name = Text(gui,height=2,width=10)
phone = Text(gui,height=2,width=10)
addButton = Button(gui,text="Add Member",width=8, height=2, command=addPerson)
alert = Button(gui,text="Click", width = 8,height=2, command =alertBox)
name_label.grid(row=0,column=0)
phone_label.grid(row=1,column=0)
name.grid(row=0,column=2)
phone.grid(row=1,column=2)
addButton.grid(row=2,column=3)
count_label.grid(row=1,column=3)
addButton.grid(row=3,column=3)
gui.mainloop()