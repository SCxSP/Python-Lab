nums = [5,1,4,3,6]
first = second = -9999999999999
    
for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num
print(nums)
print("Second Largest: ",second)
