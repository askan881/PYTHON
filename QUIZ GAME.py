question=( "1. 1+2",
           "2. 3-1",
           "3. 9*0",
           "4. 100/10",
         )

answer=(("A. 2","B. 3","C. 7","D. 5"),
        ("A. 0","B. 2","C. 1","D.6"),
        ("A. 9","B. 90","C. 0","D. 2"),
        ("A. 100","B. 20","C. 10","D. 0"))

a=("B","B","C","C")
g=[]
qn=0
score=0

for i in question[qn:5]:
    print("\n")
    print(question[qn],end="\n")
    print(answer[qn])
    n=(input("ENTER THE OPTION : ")).upper()
    g.append(n)
    if(a[qn]==g[qn]):
        print("CORRECT ANSWER .....")
        score=score+1
    else:
        print("WRONG ANSWER ......")
        print(a[qn]," IS THE RIGHT ANSWER")


    qn=qn+1 
   
print("\n")
result=((score/len(g))*100)
print("---------------------------------")
print("            RESULT               ")
print("---------------------------------")
print("YOUR ANSWERS : ",g)
print("RESULT : ",result,"%")