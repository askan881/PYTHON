def total(total):
   dc=0
   gt=0
   gst=0
   print("\n                BILLING                 ")
   b=input("DO YOU WANT DELIVERY SERVICES [Y/N] : ")
   if total>5000:
      gst=total*0.3
      if b=='y' or b=='Y':
         dc=100
         gt=total+gst+dc
      else:
         gt=total+gst
   if total<5000:
      if b=='y' or b=='Y':
         dc=100
         gt=total+dc
      else:
         gt=total

   print("\n---------------------------------------------------")
   print("|                   RECEPIT                         |")
   print("-----------------------------------------------------")
   print("CART TOTAL\t\t\t",float(total))
   print("DELIVERY CHARGE\t\t\t",dc)
   print("GST\t\t\t\t",gst)
   print("TOTAL\t\t\t\t",gt)
   print("--------------- -------------------------------------")
   
   
def dress():  
    print("----------------------------------")
    print("|             DRESS              |")
    print("|--------------------------------|")
    print("| PNO |    PRODUCT     | AMOUNT  |")
    print("|--------------------------------|")
    print("|  1  | SHIRT          |  1000   |")
    print("|  2  | PANT           |  1500   |")
    print("|  3  | JACKET         |  3000   |")
    print("|  4  | HOODIE         |  2000   |")
    print("|  5  | SHOE           |  1500   |")
    print("|  6  | BLAZER         |  3500   |")
    print("----------------------------------")
    print("|  7  |CART TOTAL                |")
    print("|  8  |EXIT                      |")
    print("----------------------------------")
    t1=0
    t2=0
    t3=0
    t4=0
    t5=0
    t6=0
    dtotal=0
    da=True
    while da:
      db=int(input("ENTER PNO TO ORDER THE ITEMS: "))
      #n=int(input(" ENTER HOW MANY ITEM : "))
      if db==1:
         n=int(input("ENTER QUANTITY OF ITEM : "))
         print("SHIRT ORDERED\n")
         t1+=1000*n
      elif db==2:
         n=int(input("ENTER QUANTITY OF ITEM : "))
         print("PANT ORDERED\n")
         t2+=1500*n
      elif db==3:
         n=int(input("ENTER QUANTITY OF ITEM : "))
         print("JACKET ORDERED\n")
         t3+=3000*n
      elif db==4:
         n=int(input("ENTER QUANTITY OF ITEM : "))
         print("HOODIE ORDERED\n")
         t4+=2000*n
      elif db==5:
         n=int(input("ENTER QUANTITY OF ITEM : "))
         print("SHOE ORDERED\n")
         t5+=1500*n
      elif db==6:
         n=int(input("ENTER QUANTITY OF ITEM : "))
         print("BLAZER ORDERED\n")
         t6+=3500*n
      elif db==7: 
         dtotal=t1+t2+t3+t4+t5+t6
         print("DRESS CART TOTAL = ",dtotal,"\n")
         ##cart(dtotal)
      elif db==8:
        print(".........................................................EXITING...................................................................\n")
        da=False
      else:
        print("INVALID INPUT")
    dtotal=t1+t2+t3+t4+t5+t6
    print("--------------------------------------------------")
    print("|        TOTAL = ",dtotal,   "                    |")
    print("--------------------------------------------------") 
    total(dtotal)



dress()