import numpy as np

marks = np.array(list(map(float, input("Enter 10 marks: ").split())))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Std Dev:", np.std(marks))
print("Variance:", np.var(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))
