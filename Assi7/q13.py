from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

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

r = float(input("Enter circle radius: "))
l, w = map(float, input("Enter rect length width: ").split())
b, h = map(float, input("Enter tri base height: ").split())

print("Circle Area:", Circle(r).area())
print("Rectangle Area:", Rectangle(l, w).area())
print("Triangle Area:", Triangle(b, h).area())
