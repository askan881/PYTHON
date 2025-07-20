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
                  ID VARCHAR(10) PRIMARY KEY,
                  CLASS VARCHAR(10) NOT NULL,
                  DOB DATE NOT NULL,
                  EMAIL VARCHAR(30) NOT NULL ,
                  PHONE_NUMBER NUMERIC)"""
            
            self.curr.execute(e)

        except Error as e:
            print("DATABASE CONNECTION FAILED...",e)
        
       
    
    def add(self):
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


    def update(self):
        up=(input("WHICH FIELD NEED TO BE UPDATED ? (NAME/ID,CLASS,DOB/EMAIL/PHONE_NUMBER) : ")).upper()
        try:
            if up=='PHONE_NUMBER':
                upcol=input("ENTER STUDENT ID :")
                upnum=int(input("ENTER NEW NUMBER : "))
                q="UPDATE STUDENT_DETAILS SET PHONE_NUMBER = %s WHERE ID = %s"
                v=(upnum,upcol)
                self.curr.execute(q,v)
                self.curr.execute("commit")

            else:
                upcol=input("ENTER STUDENT ID : ")
                upnum=(input("ENTER NEW VALUE : "))
                q=f"UPDATE STUDENT_DETAILS SET {up} = %s WHERE ID = %s"
                v=(upnum,upcol)
                self.curr.execute(q,v)
                self.curr.execute("commit")
            
            self.v=("SELECT * FROM STUDENT_DETAILS")
            self.v = self.curr.fetchall()
            for self.i in self.v:
                    print(self.i)
            print("UPDATED SUCCESSFULLY...")

            
        except Error as e:
            print("INVALID INPUT...",e)

        
    def delete(self):
        try:
            dele=input("ENTER THE STUDENT ID : ").upper()
            delcmd="DELETE FROM STUDENT_DETAILS WHERE ID= %s"
            self.curr.execute(delcmd,(dele,))
            print("DELETION SUCCESSFUL...")
            self.curr.execute("commit")
        except Error as e:
            print("DELETION FAILED...",e)
            

    
    def view(self):
        self.v=self.curr.execute("SELECT * FROM STUDENT_DETAILS")
        self.v = self.curr.fetchall()
        for self.i in self.v:
             print(self.i)


s=student()
b=True
while b:
    print("--------------------------------")
    print("|  STUDENT MANAGEMENT SYSTEM   |")
    print("--------------------------------")
    print("|1.ADD STUDENT                 |")
    print("|2.UPDATE STUDENT              |")
    print("|3.DELETE STUDENT              |")
    print("|4.VIEW STUDENT                |")
    print("|5.EXIT                        |")
    print("--------------------------------\n")
    c=int(input("ENTER YOUR CHOICE : "))
    if c==1 or c==2 or c==3 or c==4 or c==5 :
        if c==1:
            s.add()
        elif c==2:
            s.update()
        elif c==3:
            s.delete()
        elif c==4:
            s.view()
        else:
            b=False
    else:
        print("INVALID INPUT...")


