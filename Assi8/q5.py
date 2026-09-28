import array

vals = list(map(int, input("Enter numbers: ").split()))
arr = array.array('i', vals)
target = int(input("Search element: "))

if target in arr:
    print(f"Found at index: {arr.index(target)}, Occurrences: {arr.count(target)}")
else:
    print("Element not found")
