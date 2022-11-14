

products = ['peanut butter', 'jelly', 'bread']

prices = [3.99, 2.99, 1.99]

item = input("Enter the product name : ")

if item.lower() in products:
 products_index = products.index(item.lower())
 value = prices[products_index]

 print( " your product  is : " + str(item) + " is : " +str(value))

else:

 print(" Item not found")

