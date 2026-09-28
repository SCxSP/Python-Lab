class Father:
    def driving(self):
        print("Father's skill: Driving")

class Mother:
    def cooking(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    def coding(self):
        print("Child's skill: Coding")

name = input("Enter child name: ")
c = Child()
print("Child:", name)
c.driving()
c.cooking()
c.coding()
