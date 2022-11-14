
#Exercise-2.4

def average(number1, number2, number3):
    avg = (number1 + number2 + number3) / 3
    return avg


num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
average_number = average(num1, num2, num3)
print("The avg of 3 numbers are:", average_number)


