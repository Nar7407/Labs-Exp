import numpy as np

# Array creation: zeros, ones and evenly spaced values
z=np.zeros(5)               # five zeros
print(z)
o=np.ones(5)                # five ones
print(o)
a =np.linspace(0, 10, 5)    # five evenly spaced values from 0 to 10
print(a)    


# Basic statistics on a simple array
arr1 = np.array([1, 2, 3, 4, 5, 6])
print(arr1)
print("sum:", arr1.sum())
print("mean:", arr1.mean())
print("max:", arr1.max())
print("min:", arr1.min())
