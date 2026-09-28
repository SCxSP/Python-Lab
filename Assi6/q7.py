def make_counter():
    c = 0
    def count():
        nonlocal c
        c += 1
        return c
    return count

n = int(input("Enter calls: "))
counter = make_counter()
for _ in range(n):
    print("Count:", counter())
