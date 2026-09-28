class Calculator:
    def add(self, a, b, c=None):
        return a + b if c is None else a + b + c

calc = Calculator()
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print("Two numbers:", calc.add(a, b))
print("Three numbers:", calc.add(a, b, c))
