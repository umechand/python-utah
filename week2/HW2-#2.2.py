
# Exercise 2.2:

value = int(input(" Enter the number between 1 to 10: "))
if(1<=value<=10):
   if(value%2 == 0):
       print(" number is Even ")
   else:
       print(" number is odd ")

   count = 0
   for j in range(1,value+1):
       if (value%j==0):
           count +=1

   if (count==2):
       print(" Number is a prime ")
   else:
       print("  number is a not prime ")

else:
    print("Enter the number with in the range between 1 to 10 ")

