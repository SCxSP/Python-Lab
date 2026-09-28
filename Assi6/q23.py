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

r = float(input("Enter radius: "))
l, w = map(float, input("Enter length and width: ").split())
print("Circle area:", Circle(r).area())
print("Rectangle area:", Rectangle(l, w).area())
