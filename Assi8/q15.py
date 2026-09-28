import numpy as np

arr = np.array([10.0, np.nan, 20.0, 30.0, np.nan, 50.0])
print("Array:", arr)
print("NaN count:", np.isnan(arr).sum())
mean_val = np.nanmean(arr)
print("Mean ignoring NaN:", mean_val)

arr[np.isnan(arr)] = mean_val
print("Filled Array:", arr)
