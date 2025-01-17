import numpy as np

A = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]])

# Lật ma trận theo hàng
A_flipped_rows = np.flip(A, 0)
# Tương đương với np.flipud
A_flipped_rows_ud = np.flipud(A)
print("Lật ma trận theo hàng: \n", A_flipped_rows)
