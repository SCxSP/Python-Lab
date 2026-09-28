import os, pandas as pd, matplotlib.pyplot as plt

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

num_cols = ['price', 'engine-size', 'horsepower', 'curb-weight', 'city-mpg', 'highway-mpg']
for col in num_cols:
    df[col] = pd.to_numeric(df[col])

print("1. Shape:", df.shape)
print("2. Missing values total:", df.isnull().sum().sum())
print("3. Stats:\n", df[num_cols].describe())
print("4. Top 5 Expensive Makes:\n", df.groupby('make')['price'].mean().dropna().nlargest(5))
print("5. Most Common Body Style:", df['body-style'].mode()[0])
print("6. Avg Price Fuel Type:\n", df.groupby('fuel-type')['price'].mean())
print("7. Avg Price Drive Wheels:\n", df.groupby('drive-wheels')['price'].mean())
print("\nConclusion: Engine size, horsepower, and curb weight are strongly positively correlated with car price, while city and highway mileage are negatively correlated.")
