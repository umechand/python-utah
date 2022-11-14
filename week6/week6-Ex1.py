
#week 6
#Exercise-1

#1
first_name = input("Enter your first name: ").title()
middle_name = input("Enter your middle Initial: ").title()
last_name = input("Enter your last name: ").title()
print("Full name is : {} {} {}".format(first_name, middle_name, last_name))

#2
#a)
print("\"Welcome to O'Neil's Boat Rentals!\"")

#b)
print("Hello there!\nHow are you?\nI'm doing fine.")

#3
word = 'hello python'
print(word.upper())

#4
while True:
    age = input("Enter your age: ")
    if age.isdecimal() == True:
        break
    else:
        continue

#5
first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
print("* {} {} ".format(first_name, last_name)[:25] + " *")
