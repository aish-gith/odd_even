import calculator as c 


    
loop = 1
choice = 0
while loop == 1:
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit calculator")
    choice=int(input("enter ur choice:"))
    if choice == 1:
        x=float(input("enter first number:"))
        y=float(input("enter second number: "))

        z=c.add(x,y)
        print("addition result:",z)
        
    elif choice == 2:
        x=float(input("enter first number:"))
        y=float(input("enter second number: "))
        w=c.sub(x,y)
        print("subtraction result:",w)

       
    elif choice == 3:
        x=float(input("enter first number:"))
        y=float(input("enter second number: "))
        u=c.mul(x,y)
        print("multiplication result:",u)
    

        
    elif choice == 4:
        x=float(input("enter first number:"))
        y=float(input("enter second number: "))
        v=c.div(x,y)
        print("division result:",v)

        
    elif choice == 5:
        loop = 0
         













