import os, pandas as pd, matplotlib.pyplot as plt

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

df['engine-size'] = pd.to_numeric(df['engine-size'])
df['price'] = pd.to_numeric(df['price'])
clean = df.dropna(subset=['engine-size', 'price'])

corr = clean['engine-size'].corr(clean['price'])
print("Correlation Engine Size vs Price:", corr)

plt.scatter(clean['engine-size'], clean['price'], color='blue')
plt.title(f"Engine Size vs Price (Corr: {corr:.2f})")
plt.xlabel("Engine Size")
plt.ylabel("Price ($)")
plt.show()
