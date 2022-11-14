
# Exercise 2.3

def tax_function(price):
    n_price = price + 0.07
    return n_price


customer_price = float(input("Enter  price of the item:"))
final_price = tax_function(customer_price)
print("Final price of  items after  tax:", final_price)

