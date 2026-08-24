Nums = [1,2,5,4,8,9,6,4,7,25,14,52,69,74,41]

Evens = []
Odds = []

for num in Nums:
    if not num % 2:
        Evens.append(num)
    else:
        Odds.append(num)
print(Nums)
print(f"Odd Nums: {Odds}\nEven Nums: {Evens}")
