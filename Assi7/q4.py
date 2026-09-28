class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)

    def diagonal(self):
        return (self.l**2 + self.w**2) ** 0.5

l = float(input("Enter length: "))
w = float(input("Enter width: "))
r = Rectangle(l, w)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
print(f"Diagonal: {r.diagonal():.2f}")
