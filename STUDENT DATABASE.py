import mysql.connector
from  mysql.connector import Error
class student:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                host='localhost',
                user='root',
                password='askan'

            )
            if self.conn.is_connected():
                print("DATABASE CONNECTED... ")
            self.curr=self.conn.cursor()
            self.curr.execute("CREATE DATABASE IF NOT EXISTS STUDENT")
            self.curr.execute("USE STUDENT")
            print("DATABASE CREATED...")

            e=""" CREATE TABLE IF NOT EXISTS STUDENT_DETAILS(
                  NAME VARCHAR(50) NOT NULL,
                  ID VARCHAR(10) NOT NULL,
                  CLASS VARCHAR(10) NOT NULL,
                  DOB DATE NOT NULL,
                  EMAIL VARCHAR(30) NOT NULL ,
                  PHONE_NUMBER NUMERIC)"""
            
            self.curr.execute(e)

        except Error as e:
            print("DATABASE CONNECTION FAILED...",e)
        
       
    
    def details(self):
        print("\nENTER STUDENT DETAILS... \n")
        name=input("ENTER STUDENT NAME : ")
        id=input("ENTER STUDENT ID : ")
        clas=input("ENTER CLASS : ")
        dob=input("ENTER DOB(YYYY-MM-DD) : ")
        email=input("ENTER STUDENT EMAIL : ")
        pn=int(input("ENTER STUDENT PHONE NUMBER : "))

        try:
            q="INSERT INTO STUDENT_DETAILS(NAME,ID,CLASS,DOB,EMAIL,PHONE_NUMBER) VALUES(%s,%s,%s,%s,%s,%s)"
            v=(name,id,clas,dob,email,pn)
            self.curr.execute(q,v)
            self.curr.execute("commit")
            print("DATA UPDATED...")

            

        except Error as e:
            print("INSERTION FAILED ...",e)


s=student()
s.details()


