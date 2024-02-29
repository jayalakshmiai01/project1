import mysql.connector
from tkinter import *
class DBManipulate:
    def __init__(self):
        print("Welcome to Db Manipulation")

    def returnMsg(self):
        return "connected"
    
    def mydbconnection(self):
        con=mysql.connector.connect(
            host="192.168.1.240",
            user="AIBATCH01",
            password="AI@123",
            database="ai_jayalakshmi"
        )
        return con
    
    def insertvalues(self,std_name,tamil,eng,math,sci,ss):
        names=std_name
        tamil=tamil
        english=eng
        maths=math
        science=sci
        social=ss

        data=self.mydbconnection()
        result=data.cursor()

        statement="INSERT INTO student_marks (name, tamil, english, maths, science, social) VALUES( "+ '"' + names + '"' + "," + str(tamil) + "," + str(english)+","+ str(maths)  +","+ str(science) +","+ str(social) + ");"
        
        result.execute(statement)

        print(statement)

        data.commit()
        return (str(result.rowcount)+"row created")
    
    # def updatevalues(self,std_name,tamil):  
    #     name=std_name
    #     tamil=tamil
      
    #     data1=self.mydbconnection()
    #     result=data1.cursor()

    #     statement="update Student_details set Name = ("+'"'+name+'"'+") where Sno = ("+str(tamil)+") ;"
    #     result.execute(statement)
    #     print(statement)

       
    #     data1.commit()

    #     return (str(result.rowcount) + " row updated")
    
    
    # def deletevalues(self,std_name):  
        
    #     name=std_name
    #     data2=self.mydbconnection()
    #     result=data2.cursor()

    #     statement="delete from Student_details where Name = ("+'"'+name+'"'+") ;"
    #     result.execute(statement)
    #     print(statement)

       
    #     data2.commit()

    #     return (str(result.rowcount) + " row deleted")