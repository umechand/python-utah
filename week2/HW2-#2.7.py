
 # Exercise 2.7:

total = 0
total_cost = 0
tax_due = 0

while(True):
    price = int(input("Enter the items price : "))
    tax = 0.07
    total_price = price + price * tax
    print("Tax of the item $ {:.2f}".format(price * tax))
    print("New price $ "+ str(total_price))
    total_cost= total_cost + total_price
    tax_due = tax_due + price * tax
    option = input(" Enter another price ? (yes or no): ")
    if (option =="yes"):
        continue
    else:
        break

print("Total_cost is $"+str(total_cost))
print("Total tax due is $ {:.2f}".format(tax_due))


