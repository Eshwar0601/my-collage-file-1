#rock paper sizor
import random

print("==================================")
print(" welcome to stone paper sizer!!!!")
print("remember 1 is stone !!")
print("remember 2 is paper !!")
print("remember 3 is sizer !!")
print("==================================")



#user input
def useinp():
    r = random.randint(1,3)
    return r
    

while True:
    r = useinp()
    x = int(input("what do u wanna throw ?"))
    if(x == 1 and r == 2):
        print("you lose because stone wins aginst paper!!")
    elif(x == 2 and r == 1):
        print("you win because paper wins aginst stone!!")
    elif(x == 1 and r == 3):
        print("you win because stone wins aginst sizer!!")
    elif(x == 3 and r == 1):
        print("you lose because sizer wins aginst paper!!")
    elif(x == 2 and r == 3):
        print("you lose because stone wins aginst paper!!")
    elif(x == 3 and r == 2):
        print("you win because stone wins aginst paper!!")
    else:
        print("u and the computer put the same values so its a draw!!")




