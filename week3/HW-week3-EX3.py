#Exercise #3:
#Sales for the week: [100,200,300,400,500,600,700]

sales = []

for i in range(1,8):
    inp = "Enter sales for Day # "+str(i)+": "
    t = int(input(inp))
    sales.append(t)

print("Sales for the week: "+str(sales))

