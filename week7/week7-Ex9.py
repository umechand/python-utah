
#EXERCISE 9.1


class Collatz:
    def __init__(self, num):
        self.num = num

    def collatz(self):
        if self.num % 2 == 0:
            print(f"The number {self.num} is even")
            return print(self.num // 2)

        else:
            print(f"The number {self.num} is odd")
            return print((3 * self.num) + 1)


user_num = int(input("Enter a number:"))
n = Collatz(user_num)
n.collatz()


#EXERCISE 9.2


class Collatz:
    def __init__(self, num):
        self.num = num

    def collatz(self):
        while self.num != 1:
            print(f"The num {self.num} not equal to 1, calling function again!")
            if self.num % 2 == 0:
                self.num = self.num // 2

            else:
                self.num = 3 * self.num + 1
        return self.num


user_num = int(input("Enter a number:"))
n = Collatz(user_num)
res = n.collatz()
print("The result is now:", res)
print("End.")

