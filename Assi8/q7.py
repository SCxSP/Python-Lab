import numpy as np

arr = np.arange(1, 21)
print("Array:", arr)
print("First 5:", arr[:5])
print("Last 5:", arr[-5:])
print("Alternate:", arr[::2])
idx = int(input("Enter index to inspect: "))
print(f"Element at {idx}:", arr[idx])
