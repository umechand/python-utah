
#Exercise #2::

grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
print("Grades are", grades)
N_points = 0

for i in grades:
    if i >= 90:
        N_points = N_points
    elif i >= 80 and i < 90:
        N_points = N_points + 2
    elif i >= 70 and i < 80:
        N_points = N_points + 5
    else:
        N_points = N_points + 8

print("New grades are  : "+str(N_points))

