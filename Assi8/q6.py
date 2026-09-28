import numpy as np

n = int(input("Enter size for 1D array: "))
a1 = np.arange(n)
a2 = np.zeros((2, 3))
a3 = np.ones((2, 3))

print("1D:", a1, "Shape:", a1.shape)
print("Zeros 2D:\n", a2, "Shape:", a2.shape)
print("Ones 2D:\n", a3, "Shape:", a3.shape)
