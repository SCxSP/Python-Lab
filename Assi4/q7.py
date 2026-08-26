p = a = 0
for i in range(10):
    att = input(f"Student {i+1} (P/A): ").upper()
    if att == 'P':
        p += 1
    elif att == 'A':
        a += 1
print("Present:", p)
print("Absent:", a)
