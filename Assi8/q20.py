import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, np.nan, 90, 65],
    'Attendance': [85, 90, np.nan, 82]
}
df = pd.DataFrame(data)

print("Missing Values:\n", df.isnull().sum())
print("Dropna:\n", df.dropna())
print("Fillna with mean:\n", df.fillna(df.mean(numeric_only=True)))
