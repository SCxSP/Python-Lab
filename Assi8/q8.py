import numpy as np

a = np.array(list(map(float, input("Enter array 1: ").split())))
b = np.array(list(map(float, input("Enter array 2: ").split())))

print("Add:", a + b)
print("Sub:", a - b)
print("Mul:", a * b)
print("Div:", a / b)
print("Mod:", a % b)
print("Pow:", a ** b)
