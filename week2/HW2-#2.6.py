
# Exercise 2.6:


while(True):

    item_price = int(input("Enter the price of  items: "))
    tax = 0.07
    new_price = item_price + item_price * tax
    print("Tax on this item is {:.2f}".format(item_price * tax))
    print("New Price after tax is $ "+str(new_price))
    ch = input("Enter another price? (yes or no): ")

    if (ch == "yes"):

        continue
    else:

        break



