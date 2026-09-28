import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Student': [f'S{i}' for i in range(1, 11)],
    'Math': np.random.randint(60, 100, 10),
    'Physics': np.random.randint(60, 100, 10),
    'Chemistry': np.random.randint(60, 100, 10),
    'CS': np.random.randint(60, 100, 10)
}
df = pd.DataFrame(data)
subjects = ['Math', 'Physics', 'Chemistry', 'CS']
avg_marks = df[subjects].mean()
print("Subject Averages:\n", avg_marks)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(subjects, avg_marks, color='skyblue')
plt.title("Subject Averages")
plt.ylabel("Marks")

plt.subplot(1, 2, 2)
df['Total'] = df[subjects].sum(axis=1)
plt.hist(df['Total'], bins=5, color='coral', edgecolor='black')
plt.title("Total Marks Distribution")
plt.xlabel("Total Marks")

plt.tight_layout()
plt.show()
