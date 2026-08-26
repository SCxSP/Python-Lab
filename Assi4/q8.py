tot = high = 0
for i in range(10):
    amt = float(input(f"Day {i+1} savings: "))
    tot += amt
    if amt > high:
        high = amt
print("Total:", tot)
print("Highest:", high)
