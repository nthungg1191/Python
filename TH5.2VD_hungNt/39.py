import numpy as np

# Tạo một ma trận 5x5
A = np.arange(1, 26).reshape(5, 5)

# Lật ngược ma trận A theo cột
A1 = np.flip(A, axis=1)  # Tương đương với np.fliplr(A)
print("Lật ma trận A theo cột:\n", A1)

# Lật ngược ma trận A theo hàng
A2 = np.flip(A, axis=0)  # Tương đương với np.flipud(A)
print("Lật ma trận A theo hàng:\n", A2)