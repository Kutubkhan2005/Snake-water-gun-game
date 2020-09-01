#Importing random comment
import random
A=["s","w","g"]
total_chance=10
chance=0
c_point=0
h_point=0
print("Snake ,water ,gun game")
print("s for snake\nw for water\ng for gun")
while chance<total_chance:
    b=input("Snake , water , gun chose any one\n")
    c=random.choice(A)
    #----------It is when user and comp chooses same---------
    if b==c:
        print("It is a tie")
    #----------It is when user choose s and comp choose w----------
    elif b=="s" and c=="w":
        h_point=h_point+1
        print(f"Your guess is\t{b} and computer guess is\t{c}")
        print("You win one point")
        print(f"Your point is {h_point} and comp. point is {c_point}")
    #----------It is when user choose s and comp choose g----------
    elif b=="s" and c=="g":
        c_point=c_point+1
        print(f"Your guess is\t{b} and computer guess is\t{c}")
        print("Comp win one point")
        print(f"Your point is {h_point} and comp. point is {c_point}") 
    #----------It is when user choose w and comp choose s----------
    elif b=="w" and c=="s":
        c_point=c_point+1
        print(f"Your guess is\t{b} and computer guess is\t{c}")
        print("Comp win one point")
        print(f"Your point is {h_point} and comp. point is {c_point}")
    #----------It is when user choose w and comp choose g----------
    elif b=="w" and c=="g":
        h_point=h_point+1
        print(f"Your guess is\t{b} and computer guess is\t{c}")
        print("You win one point")
        print(f"Your point is {h_point} and comp. point is {c_point}")
    #----------It is when user choose g and comp choose w----------
    elif b=="g" and c=="w":
        c_point=c_point+1
        print(f"Your guess\t{b} and computer guess is\t{c}")
        print("Comp win one point")
        print(f"Your point is {h_point} and comp. point is {c_point}")
    #----------It is when user choose g and comp choose s----------
    elif b=="g" and c=="s":
        h_point=h_point+1
        print(f"Your guess is\t{b} and computer guess is\t{c}")
        print("You win one point")
        print(f"Your point is {h_point} and comp. point is {c_point}")
    else:
        print("Invalid input")
    chance=chance+1
    print(f"{total_chance-chance} no. of chance is left out of {total_chance}\n")
print("Game Over")
if c_point>h_point:
    print("You lose the game")
elif h_point>c_point:
    print("You won the game")
else :
    print("It was a tie")
print(f"Your total point are {h_point} and comp. point are {c_point} ")
