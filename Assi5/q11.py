def power(base, exponent=2):
    return base ** exponent

b = float(input("Enter base: "))
e = float(input("Enter exponent: "))

print("With default exp:", power(b))
print("With custom exp:", power(b, e))
