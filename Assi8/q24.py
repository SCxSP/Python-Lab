import matplotlib.pyplot as plt

months = list(range(1, 13))
temps = [15, 18, 22, 26, 30, 34, 32, 31, 28, 24, 19, 16]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

ax1.plot(months, temps, marker='o', color='r')
ax1.set_title("Line Plot")
ax1.set_xlabel("Month")
ax1.set_ylabel("Temp (°C)")

ax2.bar(months, temps, color='orange')
ax2.set_title("Bar Chart")
ax2.set_xlabel("Month")

ax3.scatter(months, temps, color='green')
ax3.set_title("Scatter Plot")
ax3.set_xlabel("Month")

plt.tight_layout()
plt.show()
