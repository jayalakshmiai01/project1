from tkinter import *
import mysql.connector
doc=Tk()
doc.title("operations")
doc.geometry("500x500+500+100")
doc.state("zoomed")


producttiltle=Label(doc,text="STUDENT_MARKS",fg="blue")
producttiltle.grid(row=0,column=20,padx=200,pady=30)

message=Label(doc,text="TAMIL",fg="blue")
message.grid(row=1,column=10)

producta=Entry(doc,width=60)
producta.grid(row=1,column=20)


message=Label(doc,text="ENGLISH",fg="blue")
message.grid(row=2,column=10)

productb=Entry(doc,width=60)
productb.grid(row=2,column=20)

message=Label(doc,text="MATHS",fg="blue")
message.grid(row=3,column=10)

producta=Entry(doc,width=60)
producta.grid(row=3,column=20)

message=Label(doc,text="SCIENCE",fg="blue")
message.grid(row=4,column=10)

producta=Entry(doc,width=60)
producta.grid(row=4,column=20)

message=Label(doc,text="SOCIAL",fg="blue")
message.grid(row=5,column=10)

producta=Entry(doc,width=60)
producta.grid(row=5,column=20)


click=Button(doc,text="INSERT", command=insert,fg="blue")
click.grid(row=6, column=4,padx=40,pady=40)

click=Button(doc,text="UPDATE", command=update,fg="blue")
click.grid(row=6, column=5,padx=40,pady=40)

click=Button(doc,text="DELETE", command=delete,fg="blue")
click.grid(row=6, column=6,padx=40,pady=40)

click=Button(doc,text="RESET", command=reset,fg="blue")
click.grid(row=6, column=7,padx=40,pady=40)


click=Button(doc,text="SUMBIT", command=submit,fg="blue")
click.grid(row=7, column=7,padx=40,pady=40)

doc.mainloop()

