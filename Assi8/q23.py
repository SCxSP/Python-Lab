import matplotlib.pyplot as plt

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
marks = [85, 90, 78, 92, 88]

bars = plt.bar(students, marks, color='teal')
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom', ha='center')

plt.show()
