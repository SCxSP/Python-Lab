def rev_num(n, r=0):
    return r if n == 0 else rev_num(n // 10, r * 10 + n % 10)

n = int(input("Enter no: "))
print("Reversed:", rev_num(n))
