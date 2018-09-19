#dice program
import random


i = 0
while True:
    x = int(input("press 1 to roll and 0 to quit"))
    if(x==1):
        print(random.randint(1,6))
    else:
        print("sorry u lose")
        exit()










