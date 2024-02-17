from tkinter import *
win=Tk()
win.title("operations")
win.geometry("500x500+500+100")
win.state("zoomed")

def names():
    namea=str(name1.get())
    nameb=str(name2.get())
    
    result.config(text=concate)

def login():

producttiltle=Label(win,text="concatination",fg="blue",font=("Britannic Bold",20))
producttiltle.grid(row=0,column=20,padx=200,pady=30)

message=Label(win,text="username:",fg="blue",font=("Britannic Bold",20))
message.grid(row=1,column=20)

name1=Entry(win,width=60)
name1.grid(row=1,column=25)


message=Label(win,text="password:",fg="blue",font=("Britannic Bold",20))
message.grid(row=2,column=20)

name2=Entry(win,width=60)
name2.grid(row=2,column=25)

result=Label(win,text=" ")
result.grid(row=3,column=30, pady=20)


click=Button(win,text="login", command=names,fg="blue",font=("Britannic Bold",20))
click.grid(row=4, column=1)


win.mainloop()