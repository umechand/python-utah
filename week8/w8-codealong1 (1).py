#week 8
#code along -1
#PART : 1

class Animal:

    def __init__(self):
        print("Animal class created.")

    def whoamI(self):
        print("I am an animal.")

    def eat(self):
        print("I am eating")

    def speak(self):
        raise NotImplementedError("Child class must implement this abstact method")


class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self)
        print("Dog class created")
        self.name = name

    def whoamI(self):
        print("I am a dog.")

    def speak(self):
        return self.name + " says bark!"


class Cat(Animal):

    def __init__(self, name):
        Animal.__init__(self)
        print("Cat class created")
        self.name = name

    def whoamI(self):
        print("I am a Cat.")

    def speak(self):
        return self.name + " says meow!"


dog = Dog("Murphy")
dog.whoamI()
print(dog.speak())
dog.eat()

cat = Cat("Kitty")
cat.whoamI()
print(cat.speak())
cat.eat()

#polymorphiosm example
def pet_speak(pet):
    print(pet.speak())

pet_speak(cat)
pet_speak(dog)
