import os, pandas as pd, matplotlib.pyplot as plt

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

es = pd.to_numeric(df['engine-size']).dropna()
print("Min:", es.min())
print("Max:", es.max())
print("Mean:", es.mean())
print("Median:", es.median())

plt.hist(es, bins=10, color='green', edgecolor='black')
plt.title("Engine Size Distribution")
plt.xlabel("Engine Size")
plt.show()
