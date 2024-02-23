from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into MySQL DB Demo")
win.geometry("300x300")

class frameDBoperations:
    def __init__(self):
        frametop=Frame(win,bg="black",width=800,height=300,padx=10,pady=10)
        frametop.pack(side=TOP)
        insertbtn=Button(frametop,text="INSERT") .pack(padx=10, pady=10)
        updatebtn=Button(frametop,text="UPDATE") .pack(padx=10, pady=10)
        deletebtn=Button(frametop,text="DELETE").pack(padx=10, pady=10)

    
run=frameDBoperations()
win.mainloop()       
