#2 Shopping Total

tax = 8.875 / 100
total = 0
price = 0
item = input("Enter the item name:")
while item.lower() != "done":
    price = float(input("Enter the price of the item:"))
    while price < 0:
        price = float(input("Enter the correct price:"))
    total = total + price
    item = input("Enter next item name:")
total_price = round(total + tax * total, 2)
print(f"Total amount: {total_price}")



