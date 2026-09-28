import array

arr = array.array('i', list(map(int, input("Enter initial numbers: ").split())))
print("Original:", arr.tolist())

pos = int(input("Insert pos: "))
val = int(input("Insert val: "))
arr.insert(pos, val)

app_val = int(input("Append val: "))
arr.append(app_val)

rem_val = int(input("Remove val: "))
if rem_val in arr:
    arr.remove(rem_val)

print("Updated:", arr.tolist())
