import numpy as np

arr = np.arange(1, 25)
print("Original shape:", arr.shape)
print("2x12 shape:", arr.reshape(2, 12).shape)
print("3x8 shape:", arr.reshape(3, 8).shape)
print("4x6 shape:", arr.reshape(4, 6).shape)
print("6x4 shape:", arr.reshape(6, 4).shape)
