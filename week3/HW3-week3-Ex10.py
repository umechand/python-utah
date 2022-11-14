
Exercise #10:

students = int(input("Enter no of students : "))
for s in range(1,students+1):
    a = []
    print("Students #"+str(s))
    assignments = int(input(" Enter number of assignments: "))
    for i in range(1,assignments+1):
        message = "Assignment marks are # "+str(i)+": "
        total = int(input(message))
        a.append(total)
    print("final  marks of the  student #"+str(s)+" : "+str(sum(a)))

