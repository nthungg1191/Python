import numpy as np

# Đọc dữ liệu từ file Temp.txt
# Giả sử dữ liệu được lưu dạng ma trận số trong file text
data_numpy = np.loadtxt('Temp.txt')

# In ra mảng numpy
print(data_numpy)

# In dấu gạch ngang để phân cách
print('-' * 40)

# In kích thước biến (số hàng, số cột)
print('Kích thước biến:', data_numpy.shape)

# In số chiều của biến
print('Số chiều của biến:', data_numpy.ndim)

# In kiểu dữ liệu của các phần tử
print('Kiểu dữ liệu của các phần tử:', data_numpy.dtype)

# In số phần tử
print('Số phần tử:', data_numpy.size)