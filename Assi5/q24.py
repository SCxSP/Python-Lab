def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter n: "))
for x in generate_numbers(n):
    print(x)
