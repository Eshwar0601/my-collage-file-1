import random

count = 0

def rolldie(x):
    x = input("press r to roll a die and q to quit")
    if(x == 'r'):
        print(random.randint(1,6))
    elif(x== 'q'):
        print("bye!")
    else:
        print("press a valied key!!!")
    


while True:
    rolldie('x')
    if('x' == 8):
        print("yey YOU got a ladder!!")
    elif('x' == 11):
        print("YOU got a snake!!")
    elif('x' == 13):
        print("yey YOU got a ladder!!")
    elif('x' == 25):
        print("YOU got a snake!!")
    elif('x' == 38):
        print("YOU got a snake!!")
    elif('x' == 40):
        print("yey YOU got a ladder!!")
    elif('x' == 52):
        print("yey YOU got a ladder!!")
    elif('x' == 65):
        print("YOU got a snake!!")
    elif('x' == 76):
        print("yey YOU got a ladder!!")
    elif('x' == 89):
        print("YOU got a snake!!")
    elif('x' == 93):
        print("YOU got a snake!!")
    elif('x' == 100):
        print("you won the game!!")

    count = count + x
        




