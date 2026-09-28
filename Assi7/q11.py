class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        extra_feet = total_inches // 12
        rem_inches = total_inches % 12
        return Distance(self.feet + other.feet + extra_feet, rem_inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

f1, i1 = map(int, input("Enter d1 (feet inches): ").split())
f2, i2 = map(int, input("Enter d2 (feet inches): ").split())
d1 = Distance(f1, i1)
d2 = Distance(f2, i2)
print("Total Distance:", d1 + d2)
