nums = tuple(tuple(map(int, input(f"Enter tuple {i+1} nos: ").split())) for i in range(2))
for num in nums:
    print(sum(num))
