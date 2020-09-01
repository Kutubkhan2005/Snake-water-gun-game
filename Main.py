def getdate():
    import datetime
    return datetime.datetime.now()
def take(k):
    if k==1:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            type=(input("Type here \n"))
            with open ("Kutubkan-food.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully")    
        elif a==2:
            type=(input("Type here \n"))
            with open ("Kutubkan-exer.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully")  
    elif k==2:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            type=(input("Type here \n"))
            with open ("Mustafa-food.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully")    
    
        elif a==2:
            type=(input("Type here \n"))
            with open ("Mustafa-exer.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully") 
    elif k==3:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            type=(input("Type here \n"))
            with open ("Sugra-food.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully")    
    
        elif a==2:
            type=(input("Type here \n"))
            with open ("Sugra-exer.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully")
    elif k==4:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            type=(input("Type here \n"))
            with open ("Hasan-food.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully")    
    
        elif a==2:
            type=(input("Type here \n"))
            with open ("Hasan-exer.txt", "a") as f:
                op.write(str([str(getdate())])+":"+ type+ "\n"
            print("Written successfully")        
    else :
        print("Invalid Input")
def retrive(k):
    if k==1:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            with open ("Kutubkhan-food.txt") as f:
                for i in f:
                    print(i , end="")
        elif a==2:
            with open ("Kutubkhan-exer.txt") as f:
                for i in f:
                    print(i , end="")
    elif k==2:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            with open ("Mustafa-food.txt") as f:
                for i in f:
                    print(i , end="")
        elif a==2:
            with open ("Mustafa-exer.txt") as f:
                for i in f:
                    print(i , end="")    
    elif k==3:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            with open ("Sugra-food.txt") as f:
                for i in f:
                    print(i , end="")
        elif a==2:
            with open ("Sugra-exer.txt") as f:
                for i in f:
                    print(i , end="")
    elif k==4:
        a=int(input("Enter 1 for food and 2 for exercise"))
        if a==1:
            with open ("Hasan-food.txt") as f:
                for i in f:
                    print(i , end="")
        elif a==2:
            with open ("Hasan-exer.txt") as f:
                for i in f:
                    print(i , end="")
    else:
        print("Invalid input")
print("Health Management System")
b=int(input("Enter 1 for log and 2 for retrive")
if b==1:
    c=int(input("Enter 1 for Kutubkhan ,2 for Mustafa , 3 for Sugra ,4 for Hasan"))
    take (b)
else:
    c=int(input("Enter 1 for Kutubkhan ,2 for Mustafa , 3 for Sugra ,4 for Hasan"))
    retrive (b)


