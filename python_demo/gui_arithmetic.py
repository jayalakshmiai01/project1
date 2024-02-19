from tkinter import *
win=Tk()
win.title("OPERATIONS")
win.geometry("500x500+500+100")
win.state("zoomed")

def names():
    namea=str(name1.get())
    nameb=str(name2.get())
    concate=namea+" "+nameb
    result1.config(text=concate)

def addition():
    a=int(producta.get())
    b=int(productb.get())
    c=a+b
    result1.config(text=c)

def subtraction():
    a=int(producta.get())
    b=int(productb.get())
    c=a-b
    result1.config(text=c)

def multiplication():
    a=int(producta.get())
    b=int(productb.get())
    c=a*b
    result1.config(text=c)

def division():
    a=int(producta.get())
    b=int(productb.get())
    c=a/b
    result1.config(text=c)

def modulas():
    a=int(producta.get())
    b=int(productb.get())
    c=a%b
    result1.config(text=c)

def modulas():
    a=int(producta.get())
    b=int(productb.get())
    c=a%b
    result1.config(text=c)

                      #concatenation
producttiltle=Label(win,text="CONCATENATION",fg="blue",font=("Times New Roman",18))
producttiltle.grid(row=0,column=5,padx=100,pady=30)

message=Label(win,text="Enter a name 1:",fg="blue",font=("Times New Roman",18))
message.grid(row=1,column=5)

name1=Entry(win,width=40,font=("Times New Roman",18))
name1.grid(row=1,column=7)

message=Label(win,text="Enter a  name 2:",fg="blue",font=("Times New Roman",18))
message.grid(row=3,column=5)

name2=Entry(win,width=40,font=("Times New Roman",18))
name2.grid(row=3,column=7)

result1=Label(win,text=" ",font=("Times New Roman",18))
result1.grid(row=3,column=5, pady=20)

resutl1=Entry(win,width=20,font=("Times New Roman",18))
result1.grid(row=3,column=7,pady=20)


click=Button(win,text="concatenation", command=names,fg="blue",font=("Times New Roman",18))
click.grid(row=4, column=4)

                       #Arithmetic Operators

producttiltle=Label(win,text="ARITHMETIC OPERATIONS",fg="blue",font=("Times New Roman",18))
producttiltle.grid(row=5,column=5,padx=100,pady=30)

message=Label(win,text="Enter a value 1:",fg="blue",font=("Times New Roman",18))
message.grid(row=6,column=5)

producta=Entry(win,width=40,font=("Times New Roman",18))
producta.grid(row=6,column=7)


message=Label(win,text="Enter a value 2:",fg="blue",font=("Times New Roman",18))
message.grid(row=9,column=5)

productb=Entry(win,width=40,font=("Times New Roman",18))
productb.grid(row=9,column=7)

message=Label(win,text="OUTPUT:",fg="blue",font=("Times New Roman",18))
message.grid(row=11,column=5)

productb=Entry(win,width=40,font=("Times New Roman",18))
productb.grid(row=11,column=7)

result1=Label(win,text=" ",font=("Times New Roman",18))
result1.grid(row=11,column=5, pady=20)

resutl1=Entry(win,width=20,font=("Times New Roman",18))
result1.grid(row=11,column=7)


click=Button(win,text="+", command=addition,fg="blue",font=("Times New Roman",18))
click.grid(row=12, column=3,padx=40,pady=40)

click=Button(win,text="-", command=subtraction,fg="blue",font=("Times New Roman",18))
click.grid(row=12, column=4,padx=40,pady=40)

click=Button(win,text="*", command=multiplication,fg="blue",font=("Times New Roman",18))
click.grid(row=12, column=5,padx=40,pady=40)

click=Button(win,text="/", command=division,fg="blue",font=("Times New Roman",18))
click.grid(row=12, column=6,padx=40,pady=40)

click=Button(win,text="%", command=modulas,fg="blue",font=("Times New Roman",18))
click.grid(row=12, column=7,padx=40,pady=40)

win.mainloop()



