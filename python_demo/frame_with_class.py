

from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into MySQL DB Demo")
win.geometry("300x300")


def Mydbconnection(self):
        con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Welcome@1",
        database="ai_jayalakshmi"
        )
        return con 

class frame_with_class:
    def __init__(self):
        frametop=Frame(win, bg="gray",width=800, height=300, padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT", command=self.frameLeft).pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE",command=self.frameright).pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE",command=self.framebottom).pack(padx=10, pady=10)

        
    def frameLeft(self):
           
        
        neww=Tk()
        neww.title("Insert into MySQL DB Demo")
        neww.geometry("500x500")   
        
        frameleft=Frame(neww, bg="white",width=500, height=500, padx=30,pady=30)
        frameleft.pack(side = LEFT)


        # frameright=Frame(win, bg="red",width=500, height=500)
        # frameright.pack(side = RIGHT)

        lbl_Title_of_Operation=Label(frameleft, text="Insert into MySQL DB Demo")
        lbl_Title_of_Operation.grid(row=0,columnspan=5)

        lblName=Label(frameleft,text="Name")
        lblName.grid(row=2,column=1,padx=30,pady=10)
        lblTamil=Label(frameleft,text="Tamil")
        lblTamil.grid(row=3,column=1,padx=30,pady=10)
        lblTamil1=Label(frameleft,text="English")
        lblTamil1.grid(row=4,column=1,padx=30,pady=10)
        lblTamil1=Label(frameleft,text="Maths")
        lblTamil1.grid(row=5,column=1,padx=30,pady=10)
        lblTamil1=Label(frameleft,text="Science")
        lblTamil1.grid(row=6,column=1,padx=30,pady=10)
        lblTamil1=Label(frameleft,text="Social")
        lblTamil1.grid(row=7,column=1,padx=30,pady=10)
        lblTamil1=Label(frameleft,text="Submit")
        lblTamil1.grid(row=8,column=4,padx=30,pady=10)

        name=Entry(frameleft,width=20,font=20)
        name.grid(row=2,column=2)
        tamil=Entry(frameleft,width=20,font=20)
        tamil.grid(row=3,column=2)
        english=Entry(frameleft,width=20,font=20)
        english.grid(row=4,column=2)
        maths=Entry(frameleft,width=20,font=20)
        maths.grid(row=5,column=2)
        science=Entry(frameleft,width=20,font=20)
        science.grid(row=6,column=2)
        social=Entry(frameleft,width=20,font=20)
        social.grid(row=7,column=2)


        submitbtn=Button(frameleft,text="SUBMIT",command=neww).grid(row=8,column=4)

        # a=name.get()
        # b=tamil.get()
        # c=english.get()
        # d=maths.get()
        # e=science.get()
        # f=social.get()

    
        # e_con=Mydbconnection(self)
        # result=e_con.cursor()

        # statement="Insert into student_marks(name,tamil,english,maths,science,social)values(%s,%d,%d,%d,%d,%d);"
        # valuepass=(a,b,c,d,e,f)
        # result.execute(statement,valuepass)
        
        # e_con.commit()
        


    def frameright(self):
           
        
        doc=Tk()
        doc.title("update into MySQL DB Demo")
        doc.geometry("500x500")   
        
        frameright=Frame(doc, bg="white",width=500, height=500, padx=30,pady=30)
        frameright.pack(side = LEFT)


        # frameright=Frame(win, bg="red",width=500, height=500)
        # frameright.pack(side = RIGHT)

        lbl_Title_of_Operation=Label(frameright, text="update into MySQL DB Demo")
        lbl_Title_of_Operation.grid(row=0,columnspan=5)

        lblName=Label(frameright,text="Name")
        lblName.grid(row=2,column=1,padx=30,pady=10)
        lblTamil=Label(frameright,text="Tamil")
        lblTamil.grid(row=3,column=1,padx=30,pady=10)

        name=Entry(frameright,width=20,font=20)
        name.grid(row=2,column=2)
        tamil=Entry(frameright,width=20,font=20)
        tamil.grid(row=3,column=2)




    def framebottom(self):
           
        
        bot=Tk()
        bot.title("delete into MySQL DB Demo")
        bot.geometry("500x500")   
        
        framebottom=Frame(bot, bg="white",width=500, height=500, padx=30,pady=30)
        framebottom.pack(side = LEFT)


        # frameright=Frame(win, bg="red",width=500, height=500)
        # frameright.pack(side = RIGHT)

        lbl_Title_of_Operation=Label(framebottom, text="delete into MySQL DB Demo")
        lbl_Title_of_Operation.grid(row=0,columnspan=5)

        lblName=Label(framebottom,text="Name")
        lblName.grid(row=2,column=1,padx=30,pady=10)

        name=Entry(framebottom,width=20,font=20)
        name.grid(row=2,column=2)

run=frame_with_class()
win.mainloop()



