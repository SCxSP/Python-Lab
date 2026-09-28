def power(exp):
    def calc(base):
        return base ** exp
    return calc

exp = int(input("Enter exponent: "))
base = float(input("Enter base: "))
p = power(exp)
print("Result:", p(base))
