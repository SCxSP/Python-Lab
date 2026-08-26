pos = neg = zero = 0
for i in range(20):
    n = int(input(f"Enter no {i+1}: "))
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos, "Negative:", neg, "Zero:", zero)
