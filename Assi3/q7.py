nums = list(map(int, input("Enter nos: ").split()))
first = second = -999999
for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second Largest:", second)
