import numpy as np

print("Enter elements for two 3x3 matrices:")
a = np.array(list(map(float, input("Matrix 1 (9 values): ").split()))).reshape(3, 3)
b = np.array(list(map(float, input("Matrix 2 (9 values): ").split()))).reshape(3, 3)

print("Add:\n", a + b)
print("Sub:\n", a - b)
print("Elem Mul:\n", a * b)
print("Matrix Mul:\n", a @ b)
print("Transpose A:\n", a.T)
