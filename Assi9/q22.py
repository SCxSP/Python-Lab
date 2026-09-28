import os, pandas as pd

cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
p = 'Assi9/imports-85.data' if os.path.exists('Assi9/imports-85.data') else 'imports-85.data'
df = pd.read_csv(p, names=cols, na_values='?')

num_cols = ['price', 'engine-size', 'horsepower', 'curb-weight', 'city-mpg', 'highway-mpg']
for col in num_cols:
    df[col] = pd.to_numeric(df[col])

corr_matrix = df[num_cols].corr()
print("Correlation Matrix:\n", corr_matrix)

price_corrs = corr_matrix['price'].drop('price')
print("Strongest Positive:", price_corrs.idxmax(), f"({price_corrs.max():.2f})")
print("Strongest Negative:", price_corrs.idxmin(), f"({price_corrs.min():.2f})")
