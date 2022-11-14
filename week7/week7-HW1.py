
#Exercise1

#Explain what the following variables refer to, and their scope:

#1.Person:

"person is class,scope is global."

#2.person :

"person is instance of person class ,scope is global."

#3.surname :

"surname is a parameter passed into _init_ method, its scope is local variable."

#4.self:

"Self is a parameter passed into each instance method of the class - it will be replaced by the object object when the method is called on it. operator"
"This is a new local variable inside each of the methods - it always has the same value and is named accordingly."

#5.age (the function name) :

"age is a method of the Person class. It is a local variable in the scope of the class."

#6.age (the variable used inside the function):

"Within the scope of the age method, age is a local variable."

#7.self.email :

"It's not really a separate variable. We can refer to attributes and methods of an object using a variable that refers to the object. The operator and the attribute or method name. " \
               "Whenever the self variable is defined, we can use it to refer to an object inside its own methods."

#8.person.email :

"In the global scope our person instance is referred to by the variable name person. Wherever person is defined, we can use person.email."