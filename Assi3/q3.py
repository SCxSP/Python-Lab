temps = []
while len(temps) is not 7: 
    temps += list(map(int, input(f"Enter {7 - len(temps)} temps: ").split()))

print("Max:", max(temps), "Day:", temps.index(max(temps)) + 1)
print("Min:", min(temps), "Day:", temps.index(min(temps)) + 1)
