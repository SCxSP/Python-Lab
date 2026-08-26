s = input("Enter string: ")
d = {}
for c in s:
    d[c] = d.get(c, 0) + 1
print(d)
