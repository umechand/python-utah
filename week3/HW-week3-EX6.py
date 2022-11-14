
#Exercise #6:
#Two lists:

a = [1,2,3,4,5]

b = [2,3,10,11,12,1]

c= []

for i in a:
    for j in b:
     if(i==j):
      c.append(i)

print(c)

