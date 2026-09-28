class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

class Cow(Animal):
    def sound(self):
        print("Cow moos")

ch = input("Enter dog, cat, or cow: ").lower()
if ch == "dog":
    Dog().sound()
elif ch == "cat":
    Cat().sound()
else:
    Cow().sound()
