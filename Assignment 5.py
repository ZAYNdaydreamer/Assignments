# Class and Object Example

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Car name:", self.name)
        print("Car color:", self.color)

car1 = Car("Toyota", "Red")
car1.show()


# Encapsulation Example (hiding data)

class Student:
    def __init__(self, name):
        self.name = name
        self._grade = "A"       # protected (not fully hidden)
        self.__password = "123" # private (hidden)

    def show(self):
        print("Name:", self.name)
        print("Grade:", self._grade)

stu = Student("Ali")
stu.show()
print(stu.name)
print(stu._grade)
# print(stu.__password)  # this will give error


# Single Inheritance

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()


# Multi Level Inheritance

class Grandfather:
    def land(self):
        print("Has land")

class Father(Grandfather):
    def car(self):
        print("Has car")

class Son(Father):
    def bike(self):
        print("Has bike")

s = Son()
s.land()
s.car()
s.bike()


# Multiple Inheritance

class Mom:
    def cook(self):
        print("Mom cooks food")

class Dad:
    def work(self):
        print("Dad goes to office")

class Child(Mom, Dad):
    def play(self):
        print("Child plays game")