import pandas as pd

marks = list(map(int, input("Enter 10 student marks: ").split()))
s = pd.Series(marks)

print("Series:\n", s)
print("Index:", s.index)
print("Values:", s.values)
print("First 5:\n", s.head(5))
print("Last 3:\n", s.tail(3))
print("Max:", s.max(), "Min:", s.min())
