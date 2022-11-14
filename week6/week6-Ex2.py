
#week 6
#Exercise 2

#1
def divide():
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    try:
        result = x / y
        print(round(result,4))
    except ZeroDivisionError:
        print("invalid argument")

divide()


#2
try:
    for k in ['a','b','c']:
        print(k**2)
except:
    print("An error occurred!")


#3
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Error!")
finally:
    print("All Done.")


#4
def function():
    while True:
        try:
            A = int(input("Enter an integer value: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            break

    print("Square of the number is ", A ** 2)

function()

