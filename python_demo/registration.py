
from tkinter import *
reg=Tk()
reg.geometry("500x500")

def getvalues():
    print("Accepted")

Label(reg,text="REGISTRATION FORM",font="ar 16 bold").grid(row=0,column=3)

name=Label(reg,text="name")
phoneNo=Label(reg,text="phoneNo")
gender=Label(reg,text="gender")
emergency=Label(reg,text="emergency")
paymentMode=Label(reg,text="payment Mode")

name.grid(row=1,column=2)
phoneNo.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentMode.grid(row=5,column=2)

namevalue=StringVar
phoneNovalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentModevalue=StringVar
checkvalue=int 

nameEntry=Entry(reg,textvariable=namevalue)
phoneNoEntry=Entry(reg,textvariable=phoneNovalue)
genderEntry=Entry(reg,textvariable=gendervalue)
emergencyEntry=Entry(reg,textvariable=emergencyvalue)
paymentModeEntry=Entry(reg,textvariable=paymentModevalue)

nameEntry.grid(row=1,column=3)
phoneNoEntry.grid(row=2,column=3)
genderEntry.grid(row=3,column=3)
emergencyEntry.grid(row=4,column=3)
paymentModeEntry.grid(row=5,column=3)

checkbutton=Checkbutton(text="reminder me?",variable=checkvalue)
checkbutton.grid(row=6,column=3)

Button(text="submit",command=getvalues).grid(row=7,column=3)

reg.mainloop()
