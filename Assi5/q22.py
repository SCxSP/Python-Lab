nums = list(map(int, input("Enter 5 nos: ").split()))
it = iter(nums)

for _ in range(len(nums)):
    print(next(it))

try:
    print(next(it))
except StopIteration:
    print("StopIteration reached")
