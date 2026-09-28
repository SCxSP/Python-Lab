import pandas as pd

data = {
    'Dept': ['IT', 'HR', 'IT', 'Sales', 'HR', 'Sales'],
    'Name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Salary': [60000, 50000, 80000, 45000, 55000, 48000],
    'Exp': [2, 3, 5, 1, 4, 2]
}
df = pd.DataFrame(data)
grp = df.groupby('Dept')['Salary']

print("Avg Salary:\n", grp.mean())
print("Max Salary:\n", grp.max())
print("Min Salary:\n", grp.min())
print("Employee Count:\n", grp.count())
