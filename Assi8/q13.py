import numpy as np

deg = np.array(list(map(float, input("Enter angles in degrees: ").split())))
rad = np.radians(deg)

print("Sin:", np.sin(rad))
print("Cos:", np.cos(rad))
print("Tan:", np.tan(rad))

nums = np.array([1, 4, 9, 16])
print("Sqrt:", np.sqrt(nums))
print("Log:", np.log(nums))
print("Exp:", np.exp(nums))
