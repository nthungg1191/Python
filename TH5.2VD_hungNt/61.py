import numpy as np

# Khai báo ma trận A
A = np.array([
    [-1, 2, 0, 4, 5, -3],
    [3, -7, 2, 1, 8, 4],
    [0, 5, 9, 6, 3, 1],
    [4, 9, -2, 4, -4, -7]
])

# Tìm ma trận chuyển vị của ma trận A
A_T = A.T
print('Ma trận A:\n', A)
print('Ma trận chuyển vị của A:\n', A_T)
