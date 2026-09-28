class Shape:
    def display(self):
        print("Calculating Shape Area")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.142 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h

r = Circle(float(input("Circle radius: ")))
rect = Rectangle(float(input("Rect length: ")), float(input("Rect width: ")))
tri = Triangle(float(input("Tri base: ")), float(input("Tri height: ")))

print("Circle Area:", r.area())
print("Rectangle Area:", rect.area())
print("Triangle Area:", tri.area())
