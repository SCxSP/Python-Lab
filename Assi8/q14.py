import numpy as np

a = np.array(list(map(int, input("Enter array a: ").split())))
b = np.array(list(map(int, input("Enter array b: ").split())))

print("Concatenate:", np.concatenate((a, b)))
print("Vstack:\n", np.vstack((a, b)))
print("Hstack:", np.hstack((a, b)))
print("Split a in 2:", np.array_split(a, 2))
