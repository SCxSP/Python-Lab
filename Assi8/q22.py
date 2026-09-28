import matplotlib.pyplot as plt

months = range(1, 13)
sales = [12000, 15000, 14000, 18000, 20000, 22000, 21000, 25000, 24000, 28000, 30000, 32000]

plt.plot(months, sales, marker='o', color='b', linestyle='-')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()
