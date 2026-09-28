import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Sam', 'Raj', 'Anu', 'Leo', 'Mia'],
    'Dept': ['HR', 'IT', 'IT', 'Sales', 'HR'],
    'Salary': [50000, 85000, 72000, 45000, 90000]
}
df = pd.DataFrame(data)

print("Sorted Ascending:\n", df.sort_values(by='Salary'))
print("Sorted Descending:\n", df.sort_values(by='Salary', ascending=False))
print("Highest Paid:\n", df.loc[df['Salary'].idxmax()])
print("Lowest Paid:\n", df.loc[df['Salary'].idxmin()])
df['Rank'] = df['Salary'].rank(ascending=False)
print("Ranked:\n", df)
