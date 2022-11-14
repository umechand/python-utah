
  # Exercise 2.2

def power():
    number1 = int(input("Enter 1st number:"))
    number2 = int(input("Enter 2nd number:"))
    output = 1
    if number2 == 0:
        return output
    elif number2 == 1:
        output = number1
        return output
    else:
        for i in range(number2):
            output *= number1
        return output


res = power()
print("Result=", res)

