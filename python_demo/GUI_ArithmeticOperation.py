from tkinter import *
win=Tk()
win.title("operations")
win.geometry("500x500+500+100")
win.state("zoomed")

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


producttiltle=Label(win,text="ARITHMETIC OPERATIONS",fg="blue")
producttiltle.grid(row=0,column=20,padx=200,pady=30)

message=Label(win,text="Enter a value 1:",fg="blue")
message.grid(row=1,column=10)

producta=Entry(win,width=60)
producta.grid(row=1,column=20)


message=Label(win,text="Enter a value 2:",fg="blue")
message.grid(row=2,column=10)

productb=Entry(win,width=60)
productb.grid(row=2,column=20)

result1=Label(win,text=" ")
result1.grid(row=3,column=10, pady=20)

resutl1=Entry(win,width=20)
result1.grid(row=3,column=20,pady=20)


click=Button(win,text="+", command=addition,fg="blue")
click.grid(row=4, column=4,padx=40,pady=40)

click=Button(win,text="-", command=subtraction,fg="blue")
click.grid(row=4, column=5,padx=40,pady=40)

click=Button(win,text="*", command=multiplication,fg="blue")
click.grid(row=4, column=6,padx=40,pady=40)

click=Button(win,text="/", command=division,fg="blue")
click.grid(row=4, column=7,padx=40,pady=40)

click=Button(win,text="%", command=modulas,fg="blue")
click.grid(row=4, column=8,padx=40,pady=40)

win.mainloop()





# from tkinter import *

# win=Tk()

# win.title("Arithmatic Operations")
# win.geometry("500x500+500+100")
# win.state("zoomed")

# def addition():
#     a=int(tbEntrya.get())
#     b=int(tbEntryb.get())
#     #print(a+b)
#     c=a+b
#     labelouptut.config(text=c)

# def Subtraction():
#     a=int(tbEntrya.get())
#     b=int(tbEntryb.get())
#     #print(a+b)
#     c=a-b
#     labelouptut.config(text=c)



# labelTitle=Label(win,text="Arithmatic Operations")
# labelTitle.grid(row=0,column=20,padx=200, pady=30)

# label1msg=Label(win,text="Enter value a :")
# label1msg.grid(row=1,column=20)

# tbEntrya=Entry(win,width=60)
# tbEntrya.grid(row=1,column=25)


# label2msg=Label(win,text="Enter value b :")
# label2msg.grid(row=2,column=20, pady=20)

# tbEntryb=Entry(win,width=60)
# tbEntryb.grid(row=2,column=25,pady=20)


# labelouptut=Label(win,text="")
# labelouptut.grid(row=3,column=30, pady=20)


# btnAdd=Button(win,text="Addition", command=addition)
# btnAdd.grid(row=4, column=1)

# btnSubtract=Button(win,text="Subtraction",command=Subtraction)
# btnSubtract.grid(row=4,column=2)



# win.mainloop()