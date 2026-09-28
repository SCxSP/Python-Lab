import os, pandas as pd, matplotlib.pyplot as plt

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

hw = pd.to_numeric(df['highway-mpg']).dropna()
print("Min:", hw.min())
print("Max:", hw.max())
print("Mean:", hw.mean())
print("Median:", hw.median())

plt.hist(hw, bins=10, color='cyan', edgecolor='black')
plt.title("Highway MPG Distribution")
plt.xlabel("Highway MPG")
plt.show()
