import mysql.connector
from tkinter import *
class DBManipulate:
    def __init__(self):
        print("Welcome to Db Manipulation")

    def returnMsg(self):
        return "connected"
    
    def mydbconnection(self):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Welcome@1",
            database="ai_jaya"
        )
        return con
    
    def insertvalues(self,std_name,tamil,eng,math,sci,ss):
        name=std_name
        tamil=tamil
        english=eng
        maths=math
        science=sci
        social=ss

        data=self.mydbconnection()
        result=data.cursor()

        statement="INSERT INTO student_marks (Name, Tamil, English, Maths, Science, Social) VALUES(( "+ '"' + name + '"' + "," + str(tamil) + "," + str(english)+","+ str(maths)  +","+ str(science) +","+ str(social) + ");"
        
        result.execute(statement)

        print(statement)

        data.commit
        return(str(result.rowcount)+"row created")