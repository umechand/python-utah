# code along3

import random

num1 = random.randint(0,50)
num2 = random.randint(0,50)

answer = int(input("what is the sum of " + str(num1) + " + " + str(num2)))
num_sum = num1 + num2

if (answer == num_sum):
    print("Correct!")

while num_sum != answer:
    print("Incorrect, please try again")
    answer = int(input(" what is the sum of " + str(num1) + "+ " + str(num2)))

    if (answer == num_sum):
        print("Correct!")
        break







