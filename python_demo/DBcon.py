from tkinter import *
std=Tk()
std.title("STUDENT_MARKS")
std.geometry("500x500+500+100")
std.state("zoomed")

def insert():
    pass
def update():
    pass
def delete():
    pass
def reset():
    pass
def submit():
    pass

Label(std,text="STUDENT_MARKS",font="ar 18 bold").grid(row=0,column=5)

Tamil=Label(std,text="TAMIL")
English=Label(std,text="ENGLISH")
Maths=Label(std,text="MATHS")
Science=Label(std,text="SCIENCE")
Social=Label(std,text="SOCIAL")
Total=Label(std,text="TOTAL")


Tamil.grid(row=1,column=4)
English.grid(row=2,column=4)
Maths.grid(row=3,column=4)
Science.grid(row=4,column=4)
Social.grid(row=5,column=4)
Total.grid(row=6,column=4)

Tamil=StringVar
English=StringVar
Maths=StringVar
Science=StringVar
Social=StringVar
Total=StringVar

Tamilentry=Entry(std,textvariable=Tamil)
Englishentry=Entry(std,textvariable=English)
Mathsentry=Entry(std,textvariable=Maths)
scienceentry=Entry(std,textvariable=Science)
Socialentry=Entry(std,textvariable=Social)
Totalentry=Entry(std,textvariable=Total)


Tamilentry.grid(row=1,column=5)
Englishentry.grid(row=2,column=5)
Mathsentry.grid(row=3,column=5)
scienceentry.grid(row=4,column=5)
Socialentry.grid(row=5,column=5)
Totalentry.grid(row=6,column=5)


Button(text="INSERT",command=insert).grid(row=8,column=3)
Button(text="UPDATE",command=update).grid(row=8,column=4)
Button(text="DELETE",command=delete).grid(row=8,column=5)
Button(text="RESET",command=reset).grid(row=8,column=6)
Button(text="SUBMIT",command=submit).grid(row=9,column=8)

std.mainloop()