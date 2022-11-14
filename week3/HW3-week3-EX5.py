
#Exercise #5:


products = ["apple", "pear", "peach", "banana"]

inp = input("Enter product name: ")

if inp.lower() in products:
    print("It is in our inventory")
else:
    print("Product is  not found")
