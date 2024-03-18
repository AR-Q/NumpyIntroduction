import numpy as np

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [2,3],
    [4,5]
])

dot = np.dot(a,b)

print(dot)

det = np.linalg.det(a)

print(det)

a_inverse = np.linalg.inv(a)

print(a_inverse)