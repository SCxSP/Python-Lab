import array

vals = list(map(int, input("Enter 10 integers: ").split()))
arr = array.array('i', vals)
print("Sum:", sum(arr))
print("Avg:", sum(arr) / len(arr))
print("Max:", max(arr))
print("Min:", min(arr))
print("Length:", len(arr))
