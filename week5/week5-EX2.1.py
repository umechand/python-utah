
#week5 exercise 2.1

import math

def sum_of_list(number_list):
    print("The list of numbers:", number_list)
    sum = 0
    for i in range(len(number_list)):
        sum += number_list[i]
    return sum

total = sum_of_list([5,4,3,2,1])
print("The total sum of the list:", total)

