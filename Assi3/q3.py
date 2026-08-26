temps = list(map(float, input("Enter 7 temps: ").split()))
print("Max:", max(temps), "Day:", temps.index(max(temps)) + 1)
print("Min:", min(temps), "Day:", temps.index(min(temps)) + 1)
