
# week5 Exercise4

import random

def guessthenumber():
    secretnumber = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20")



    for guessesTaken in range(1, 7):
        guess = int(input("Take a guess."))
        print(guess)
        if (guessesTaken < 6) & (guess < secretnumber):
            print("Your guess is too low.")
        elif (guessesTaken < 6) & (guess > secretnumber):
            print("Your guess is too high.")
        elif (guessesTaken < 6) & (guess == secretnumber):
            print(f"Good job! You guessed my number in {guessesTaken} gueeses!")
            break
        elif guessesTaken == 6:
            print(f"Nope. The number I was thinking of was {secretnumber}")


guessthenumber()

