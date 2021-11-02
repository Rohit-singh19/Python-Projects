import random

def gameWin(randNO,your):
    if randNO==your:
        print("The Game is Tie!")
    elif randNO=="r":
        if your=="p":
            print("You Win!")
        else:
            print("You Loss!")
    elif randNO=="p":
        if your== "s":
            print("You Win!")
        else:
            print("You Loss!")
    else:
        if your== "r":
            print("You Win!")
        else:
            print("You Loss!")


print("Rock(r), Paper(p) and scissors(s)")
print("Computer turns")
your= input("Your turns : ")
# print(your)
if your=="s":
    print("You choose : Scissor")
elif your=="r":
    print("You choose : Rock")
else:
    print("You choose : Paper")

    
randNO = random.randint(1,3)
# print(randNO)
if randNO==1:
    randNO="r"
    print("Computer choose : Rock")
elif randNO==2:
    randNO="p"
    print("Computer choose : Paper")
else:
    randNO="s"
    print("Computer choose : Scissor")

gameWin(randNO,your)
# print(randNO)