
# Exercise 2.9:


import random

num1 = random.randint(0,56)
num2 = random.randint(0,56)
sol = num1 + num2

while(1):

    msg = "Enter answer for "+str(num1)+"+"+str(num2)+" "
    answer = int(input(msg))
    if (answer == sol):
        print("your Answer is correct")
        break
    else:
        print("your  Answer is wrong ! \n Try again")
        continue


