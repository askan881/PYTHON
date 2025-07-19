 #global variable
cname=None
cpas=None
balance = 0.0

def create():
    print("\nCREATING  ACCOUNT")
    print("_______________________")
    global cname,cpas
    cname=input("ENTER NAME : ")
    cpas=input("ENTER PASSWORD : ")
    print("_______________________")
    print("ACCOUNT CREATED\n")
    
    
        

def deposit():
    deposit=float(input("ENTER AMOUNT TO DEPOSITE : "))
    print("DEPOSITE COMPLETED...")
    global balance
    balance= balance + deposit  

def withdraw():
    global balance
    if balance>0 :
      withdraw=float(input("ENTER AMOUNT TO WITHDRAW : "))
      if withdraw<=balance:
          print("WITHDRAW COMPLETED...")
          balance=balance-withdraw
      else:
          print("WITHDRAW AMOUNT IS MORE THAN BALANCE")
    else:
        print("insufficient balance")

def bbalance():
    global balance
    if ( balance >= 0):
        print("BALANCE :  ",balance)
    else:
        print("BALANCE IS EMPTY")

#second loop
def login():  
    print("\nACCOUNT LOGIN")
    print("_______________________")
    lname=input("ENTER NAME : ")
    lpas=input("ENTER PASSWORD : ")
    print("_______________________")
    print("\n")
    global cname,cpas
    if(cname==lname and cpas==lpas):
        print("______________________________________________________________________________________________________________________")
        print("                                                     WELCOME ",lname)
        print("______________________________________________________________________________________________________________________")
        l=True
        while l:
            print("\nBANK SERVICE")
            print("1.DEPOSIT")
            print("2.WITHDRAW")
            print("3.BALANCE")
            print("4.EXIT")
            c=int(input("ENTER YOUR CHOICE : "))
            if c==1:
               deposit()
            elif c==2:
               withdraw()
            elif c==3:
               bbalance()
            elif c==4:
               print("________________________________________________________________________________________________________________")
               print("                                                         THANK YOU  ",cname)
               print("________________________________________________________________________________________________________________")
               l=False
            else:
                print("INVALID CHOICE")
    else:
        print("INVALID ACCOUNT")

        
#main function 
#first loop
ll=True
while ll:
    print("\n\nBANK SERVICE")
    print("1.CREATE ACCOUNT")
    print("2.LOGIN")
    print("3.EXIT")
    a=int(input("ENTER YOUR CHOICE : "))
    if a==1:
        create()
    elif a==2:
        login()
    elif a==3:
        ll=False
    else:
        print("INVALID CHOICE")

print("EXITING ")