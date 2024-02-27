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