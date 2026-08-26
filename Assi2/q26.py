nums = [list(map(int, input(f"Enter list {i+1} nos: ").split())) for i in range(2)]
for num in nums:
    print(max(num))
