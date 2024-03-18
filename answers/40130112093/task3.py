import numpy as np

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [2,3],
    [4,5]
])

sum = np.add(a,b)
sub = np.subtract(a,b)
mul = np.multiply(a,b)
div = np.divide(a,b)

print(sum)
print(sub)
print(mul)
print(div)


three_d_array = np.ones((2,3,4))

two_d = np.reshape(three_d_array, (6,4))

flaten = two_d.flatten()

print(two_d)

print(flaten)