
#Exercise #8:

products = ["apple", "pear", "peach", "banana"]

while(1):
    list = input("Enter your product name: ")
    if list.lower() == "end" or products == []:
        break
    elif list.lower() in products:
        products.remove(list.lower())
        print(products)
    else:
        print("we do not currently carry the product")

