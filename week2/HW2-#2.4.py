
# Exercise 2.4:

start_number = int(input(" Enter the starting value"))
Ending_number = int(input(" Enter the ending value"))

value = input(" even or odd ? : ")
for j in range(start_number, Ending_number+1):
    if(value == "even"):
        if(j%2 == 0):
            print(j)
    else:
        if(j%2 != 0):
            print(j)





