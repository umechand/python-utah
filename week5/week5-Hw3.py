
# week5 Exercise3

import random

def rollstwodice(number):
    for i in range(number-5, number):
        R1 = random.randint(1, number)
        R2 = random.randint(1, number)
        print(f"{i} sided dice roll: {R1} & {R2}")



value_limit = int(input("Enter the limit:"))
while value_limit < 11:
    print("The limit should be greater or equal to 11")
    value_limit = int(input("Enter the limit:"))
rollstwodice(value_limit)



