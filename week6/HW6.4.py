
# Exercise #4:

f_name = open('testscores.txt', 'r')
score = f_name.read().splitlines()

sum = 0
count = 0
for i in score:
    if i.isdigit() == True:
        sum += int(i)
        count = count+1
        avg = sum / count

result = score[0]
print("Students name is: " ,str(result))
print("The average for the student is:", avg)

