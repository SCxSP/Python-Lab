def gen_nums(limit):
    for i in range(1, limit + 1):
        yield i

n = int(input("Enter limit (e.g. 50): "))
for x in gen_nums(n):
    if x % 3 == 0 and x % 5 == 0:
        print(x)
