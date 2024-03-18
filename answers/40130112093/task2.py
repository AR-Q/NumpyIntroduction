import numpy as np

one_d_array = np.array([4,5,6,6,4,2,2])

print(one_d_array[2])

two_d_array = np.array([
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
])

print(two_d_array[2][3])



sub_matrix = two_d_array[np.ix_([0,1],[0,1])]

print(sub_matrix)


three_d_array = np.ones((2,3,4))


for i in three_d_array:
    print(i)