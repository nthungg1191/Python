import numpy as np

# Define the matrices
a = np.array([
    [9, 4, 19, 1, 18],
    [15, 11, 1, 9, 14],
    [17, 8, 10, 4, 13]
])

b = np.array([
    [6, 4, 12, 4, 2],
    [3, 6, 11, 14, 10],
    [1, 6, 5, 12, 2]
])

# Compare the matrices element-wise
equal_ab = np.equal(a, b)
# Alternatively, you can use the '==' operator
# equal_ab = a == b

print("Element-wise comparison of a and b:")
print(equal_ab)
