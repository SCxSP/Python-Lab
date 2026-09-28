class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.142 * self.r * self.r

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

def print_area(shape):
    print("Area:", shape.area())

r = float(input("Circle radius: "))
l, w = map(float, input("Rectangle length width: ").split())
print_area(Circle(r))
print_area(Rectangle(l, w))
