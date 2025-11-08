# Parent class
class Animal:
    def speak(self):
        print("This animal makes a sound")

# Child classes with method overriding
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Example Usage
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()  # Polymorphism: same method name, different behavior



#Python doesn’t support traditional overloading, but we can achieve it using default arguments or *args / **kwargs:

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))        # 5
print(calc.add(5, 10))    # 15
print(calc.add(5, 10, 15))# 30
