import os, pandas as pd, matplotlib.pyplot as plt

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

df['price'] = pd.to_numeric(df['price'])
avg_fuel = df.groupby('fuel-type')['price'].mean()
print("Average Price by Fuel Type:\n", avg_fuel)

avg_fuel.plot(kind='bar', color=['gray', 'gold'])
plt.title("Average Price by Fuel Type")
plt.ylabel("Avg Price ($)")
plt.show()
