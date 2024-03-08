import numpy as np

one_d_array = np.array([4,5,6,6,4,2,2])

print(one_d_array)
print(np.shape(one_d_array))
print(one_d_array.dtype)
print(np.sum(one_d_array))
print("-----------------------------")

two_d_array = np.array([
    [2,5,1,6],
    [4,6,6,2],
    [7,9,0,1]
])

print(two_d_array)
print(np.shape(two_d_array))
print(two_d_array.dtype)
print(np.sum(two_d_array))
print("-----------------------------")

three_d_array = np.array([
    [
        [2,5,1,6],
        [4,6,6,2],
        [7,9,0,1]
    ],
    [
        [12,42,16,10],
        [57,44,86,23],
        [35,61,12,30]
    ]
])

print(three_d_array)
print(np.shape(three_d_array))
print(three_d_array.dtype)
print(np.sum(three_d_array))
print("-----------------------------")