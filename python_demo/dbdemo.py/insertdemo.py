from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into mySQL DB Demo")
win.geometry("500x500")

frametop=Frame(win,bg="black",width=500,height=30)
frametop.pack(side=TOP)

frameleft=Frame(win,bg="black",width=500,height=30,padx=30,pady=30)
frameleft.pack(side=LEFT)

frameright=Frame(win,bg="red",width=500,height=30)
frameright.pack(side=RIGHT)

lbl_title_Of_Operation=Label(frameleft,text="Insert Into Mysql DB Demo")
lbl_title_Of_Operation.grid(row=0,columnspan=5)

lblname=Label(frameleft,text="Name")
lblname.grid(row=2,column=1,padx=30,pady=30)


win.mainloop()