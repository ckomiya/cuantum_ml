import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = np.array([1,2,3,4,30])

print("sum elementos de a: " + str(np.sum(a)))
print("mean (media) elementos de a: " + str(np.mean(a)))
print("min elementos de a: " + str(np.min(a)))
print("max elementos de a: " + str(np.max(a)))