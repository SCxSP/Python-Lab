import array

vals = list(map(int, input("Enter numbers: ").split()))
arr = array.array('i', vals)

asc = array.array('i', sorted(arr))
desc = array.array('i', sorted(arr, reverse=True))
rev = array.array('i', reversed(arr))

print("Ascending:", asc.tolist())
print("Descending:", desc.tolist())
print("Reversed:", rev.tolist())
