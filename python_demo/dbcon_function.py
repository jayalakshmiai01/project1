from tkinter import *
import mysql.connector
doc=Tk()
doc.title("STUDENTS_MARKS")
doc.geometry("500x500+500+100")
doc.state("zoomed")

def MyDBconnection():
        
        dbconn=mysql.connector.connect(
        host="192.168.1.240",
        user="AIBATCH01",
        password="AI@123",
        database="ai_jayalakshmi"
        )
        return dbconn
        
  
    

def insert():
     
     a=name.get()
     b=tamil.get()
     c=english.get()
     d=maths.get()
     e=science.get()
     f=social.get()

     e_con=MyDBconnection()
     result=e_con.cursor()

     statement="Insert into student_marks(name,tamil,english,maths,science,social)values(%s,%s,%s,%s,%s,%s);"
     valuepass=(a,b,c,d,e,f)
     result.execute(statement,valuepass)
     
     e_con.commit()
     
     print(result.rowcount, "row inserted")

def update():
    a=name.get()
    b=tamil.get()
    c=english.get()
    d=maths.get()
    e=science.get()
    f=social.get()

    e_con=MyDBconnection()
    result=e_con.cursor()

    statement="update student_marks set name = (%s) where sno = (%s);"
    valuepass=(a,b)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount, "row updated")

    
def delete():
    
    a=name.get()

    e_con=MyDBconnection()
    result=e_con.cursor()

    statement="delete from student_marks where sno = (%s);"
    valuepass=(a,)
    result.execute(statement,valuepass)
    e_con.commit()

    print(result.rowcount, " row deleted")  
def alter():
    a=name.get()
    e_con=MyDBconnection()
    result=e_con.cursor()
    statement="alter table student_marks drop column " +str(a)+ ";"
#     valuepass=(a,)
    result.execute(statement,)
    e_con.commit()
    print(result.rowcount, " row altered")  


def submit():
     pass

title=Label(doc,text="STUDENT_MARKS",fg="blue",font=20)
title.grid(row=0,column=20,padx=200,pady=30)

language=Label(doc,text="NAME",fg="blue",font=20)
language.grid(row=1,column=10)

name=Entry(doc,width=20,font=20)
name.grid(row=1,column=20)


language=Label(doc,text="TAMIL",fg="blue",font=20)
language.grid(row=2,column=10)

tamil=Entry(doc,width=20,font=20)
tamil.grid(row=2,column=20)


language=Label(doc,text="ENGLISH",fg="blue",font=20)
language.grid(row=3,column=10)

english=Entry(doc,width=20,font=20)
english.grid(row=3,column=20)

language=Label(doc,text="MATHS",fg="blue",font=20)
language.grid(row=4,column=10)

maths=Entry(doc,width=20,font=20)
maths.grid(row=4,column=20)

language=Label(doc,text="SCIENCE",fg="blue",font=20)
language.grid(row=5,column=10)

science=Entry(doc,width=20,font=20)
science.grid(row=5,column=20)

language=Label(doc,text="SOCIAL",fg="blue",font=20)
language.grid(row=6,column=10)

social=Entry(doc,width=20,font=20)
social.grid(row=6,column=20)


click=Button(doc,text="INSERT", command=insert,fg="blue",font=20)
click.grid(row=7, column=4,padx=40,pady=40)

click=Button(doc,text="UPDATE", command=update,fg="blue",font=20)
click.grid(row=7, column=5,padx=40,pady=40)

click=Button(doc,text="DELETE", command=delete,fg="blue",font=20)
click.grid(row=7, column=6,padx=40,pady=40)

click=Button(doc,text="ALTER", command=alter,fg="blue",font=20)
click.grid(row=7, column=7,padx=40,pady=40)


click=Button(doc,text="SUBMIT", command=submit,fg="blue",font=20)
click.grid(row=8, column=8,padx=40,pady=40)




doc.mainloop()