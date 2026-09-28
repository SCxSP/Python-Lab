import os, pandas as pd, matplotlib.pyplot as plt

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

hp = pd.to_numeric(df['horsepower']).dropna()
print("Min:", hp.min())
print("Max:", hp.max())
print("Mean:", hp.mean())
print("Median:", hp.median())
print("Std Dev:", hp.std())

plt.hist(hp, bins=10, color='orange', edgecolor='black')
plt.title("Horsepower Distribution")
plt.xlabel("Horsepower")
plt.show()
