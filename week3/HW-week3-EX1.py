
#Exercise #1:

grades = [90,100,70,45,76,84,93,21,36,99,100]
print("Grades are", grades)
L = 0
M = 0
N = 0
O = 0
P = 0
Q = 0
for i in grades:
    if 90 <= i <= 100:
        L +=1
    elif 80 <= i <= 89:
        M +=1
    elif 70 <= i <= 79:
        N +=1
    elif 60 <= i <= 69:
        O +=1
    elif 50 <= i <= 59:
         P +=1
    elif i < 50:
        Q +=1

print("Number of L : ", L)
print("Number of M : ", M)
print("Number of N : ", N)
print("Number of O : ", O)
print("Number of P : ", P)
print("Number of Q : ", Q)



