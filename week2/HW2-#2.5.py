
# Exercise 2.5:

number_items = int(input("Enter the number of items: "))


c = 1
Total_amount = 0


while(c<=number_items):
    msg = "Enter the value of item #"+str(c)+" : "

    price = float(input(msg))

    Total_amount = Total_amount + price

    c+=1


print("Total price of the items is : $"+str(Total_amount))

