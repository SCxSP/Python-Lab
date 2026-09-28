import os, pandas as pd, matplotlib.pyplot as plt

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

counts = df['fuel-type'].value_counts()
perc = df['fuel-type'].value_counts(normalize=True) * 100

print("Counts:\n", counts)
print("Percentages:\n", perc)

counts.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Fuel Type Distribution")
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.show()
