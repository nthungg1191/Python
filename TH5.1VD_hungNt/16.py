import numpy as np

x = np.arange(8)
print("x =", x)
print('-------------------------')
# Sử dụng các phương thức của NumPy
print("x + 5 =", np.add(x, 5))
print("x - 5 =", np.subtract(x, 5))
print("-x =", np.negative(x))
print("x * 2 =", np.multiply(x, 2))
print("x / 2 =", np.divide(x, 2))
print("x // 2 =", np.floor_divide(x, 2))
print("x % 2 =", np.mod(x, 2))
print("x ** 3 =", np.power(x, 3))
