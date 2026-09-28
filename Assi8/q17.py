import pandas as pd

data = {
    'Roll': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Dept': ['CS', 'IT', 'CS', 'EC', 'CS', 'IT', 'EC', 'CS', 'IT', 'EC'],
    'Marks': [85, 72, 90, 65, 88, 79, 95, 60, 82, 91],
    'Attendance': [85, 90, 78, 82, 88, 92, 96, 75, 84, 89]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("Head(5):\n", df.head(5))
print("Tail(5):\n", df.tail(5))
print("Selected Cols:\n", df[['Name', 'Marks']])
roll_search = int(input("Enter Roll to inspect: "))
print(df[df['Roll'] == roll_search])
