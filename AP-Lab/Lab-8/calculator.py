#using tkinter module package
from tkinter import *

#connecting to the database
import sqlite3
conn = sqlite3.connect('calculator.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS calculator (express varchar(30), res int)''')

#statement variable to keep the input by user
expression = ""

#this function keeps track of the input and the operations by user
def press(num):
    global expression
    expression = expression + str(num)

    #updating the statement variable using set
    equation.set(expression)

#this function evaluates and returns ans to the user based on the statement
def equalpress():
    global c
    global expression
    total = str(eval(expression))
    
    #file operations
    f = open("calcfile_expressions.txt", "a")
    equation.set(total)
    exp = str(expression)+"="+str(total)+"\n"

    #databse operations
    c.execute("INSERT INTO calculator VALUES ("+str(expression)+","+total+")")
    c.execute("SELECT * FROM CALCULATOR")
    rows = c.fetchall()
    print(rows)

    f.write(exp) 

    expression = ""

# function to clear the statement
def clear():
    global expression
    expression = ""
    equation.set(expression)

# creating a GUI window 
gui = Tk() 

# setting the background colour of GUI window 
gui.configure(background="grey") 

# setting the title of GUI window 
gui.title("Calculator") 

# setting the configuration of GUI window 
gui.geometry("320x220") 

equation = StringVar()

# creating the text entry box
expression_field = Entry(gui, textvariable = equation)
expression_field.grid(columnspan = 4,ipadx = 100)

#setting equation to text 'enter your statement'
equation.set('Enter Your Statement') 

#creating buttons
button1 = Button(gui, text = '1', command = lambda: press(1), fg='white', bg='black', 
                 height=2, width=10)
button2 = Button(gui, text = '2', command = lambda: press(2), fg='white', bg='black', 
                 height=2, width=10)
button3 = Button(gui, text = '3', command = lambda: press(3), fg='white', bg='black', 
                 height=2, width=10)
button4 = Button(gui, text = '4', command = lambda: press(4), fg='white', bg='black', 
                 height=2, width=10)
button5 = Button(gui, text = '5', command = lambda: press(5), fg='white', bg='black', 
                height=2, width=10)
button6 = Button(gui, text = '6', command = lambda: press(6), fg='white', bg='black', 
                height=2, width=10)
button7 = Button(gui, text = '7', command = lambda: press(7), fg='white', bg='black', 
                 height=2, width=10)
button8 = Button(gui, text = '8', command = lambda: press(8), fg='white', bg='black', 
                 height=2, width=10)
button9 = Button(gui, text = '9', command = lambda: press(9), fg='white', bg='black', 
                 height=2, width=10)
button0 = Button(gui, text = '0', command = lambda: press(0), fg='white', bg='black', 
                 height=2, width=10)
button10 = Button(gui, text = '+', command = lambda: press("+"), fg='white', bg='black', 
                 height=2, width=10)
button11 = Button(gui, text = '-', command = lambda: press("-"), fg='white', bg='black', 
                 height=2, width=10)
button12 = Button(gui, text = '*', command = lambda: press("*"), fg='white', bg='black', 
                 height=2, width=10)
button13 = Button(gui, text = '/', command = lambda: press("/"), fg='white', bg='black', 
                 height=2, width=10)
button_clear = Button(gui, text = 'Clear', command = clear, fg='white', bg='black', 
                 height=2, width=10)
button_equal = Button(gui, text = '=', command = equalpress, fg='white', bg='black', 
                 height=2, width=10)
button_dot = Button(gui, text = '.', command = lambda: press("."), fg='white', bg='black', 
                 height=2, width=10)

#adding buttons to the GUI
button1.grid(row = 2, column = 0)
button2.grid(row = 2, column = 1)
button3.grid(row = 2, column = 2)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
button7.grid(row = 4, column = 0)
button8.grid(row = 4, column = 1)
button9.grid(row = 4, column = 2)
button0.grid(row = 5, column = 1)
button_clear.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 2)
button10.grid(row = 2, column = 3)
button11.grid(row = 3, column = 3)
button12.grid(row = 4, column = 3)
button13.grid(row = 5, column = 3)
button_dot.grid(row = 6, column = 0)

#adding the gui to mainloop
gui.mainloop()

#closing the database
conn.commit()
conn.close()