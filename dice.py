#dice
import random

x = int(input(" press 1 to roll the dice   and 0 to quit : "))
print("Do u wanna print a random number")
if(x == 1):
	print(random.randint(1,6))

if(x == 0):
	print("ok game ends here !!!")











