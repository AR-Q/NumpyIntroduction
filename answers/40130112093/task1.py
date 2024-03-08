import numpy as np

one_d_array = np.array([4,5,6,6,4,2,2])

print(one_d_array.ndim)
print(np.shape(one_d_array))
print(one_d_array.dtype)
print(np.sum(one_d_array))
print("-----------------------------")

two_d_array = np.zeros((3,4))

print(two_d_array.ndim)
print(np.shape(two_d_array))
print(two_d_array.dtype)
print(np.sum(two_d_array))
print("-----------------------------")

three_d_array = np.ones((2,3,4))

print(three_d_array.ndim)
print(np.shape(three_d_array))
print(three_d_array.dtype)
print(np.sum(three_d_array))
print("-----------------------------")