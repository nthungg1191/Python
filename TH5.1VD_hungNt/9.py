import numpy as np

# Tạo một vector từ 0 đến 5
x = np.arange(0, 6)
print("Vector ban đầu:", x)

# Tách vector thành hai phần có số phần tử bằng nhau
x1, x2 = np.split(x, 2)
print("Vector sau khi tách:", x1, x2)
