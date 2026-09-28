import pandas as pd

data = {
    'Roll': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Dept': ['CS', 'IT', 'CS', 'EC', 'CS'],
    'Marks': [85, 55, 90, 65, 78],
    'Attendance': [85, 90, 70, 82, 88]
}
df = pd.DataFrame(data)

print("Marks > 75:\n", df[df['Marks'] > 75])
print("Attendance > 80%:\n", df[df['Attendance'] > 80])
print("Marks > 60 & Attendance > 75:\n", df[(df['Marks'] > 60) & (df['Attendance'] > 75)])
dept = input("Enter dept to filter (e.g. CS): ")
print(df[df['Dept'] == dept])
