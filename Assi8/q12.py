import numpy as np

arr = np.array(list(map(int, input("Enter 20 integers: ").split())))
print("Evens:", arr[arr % 2 == 0])
print("Odds:", arr[arr % 2 != 0])
print(">50:", arr[arr > 50])
print("Between 20 and 60:", arr[(arr >= 20) & (arr <= 60)])
