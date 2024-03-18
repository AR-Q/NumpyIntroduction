import numpy as np

a = np.array([
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
])

b = np.array([
    [4,7,3,7],
    [3,5,7,7],
    [11,8,2,1]
])


mean = np.mean(a)

print(mean)


median = np.median(a)

print(median)


variance = np.var(a)

print(variance)


std = np.std(a)

print(std)



correlation = np.corrcoef(a,b)

print(correlation)