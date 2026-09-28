class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

choice = input("Enter dog or cat: ").lower()
pet = Dog() if choice == "dog" else Cat()
pet.sound()
