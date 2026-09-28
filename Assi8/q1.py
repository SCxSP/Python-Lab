import array

vals = list(map(int, input("Enter 10 integers: ").split()))
arr = array.array('i', vals)
print("Array:", arr.tolist())
print(f"First: {arr[0]}, Middle: {arr[len(arr)//2]}, Last: {arr[-1]}")
