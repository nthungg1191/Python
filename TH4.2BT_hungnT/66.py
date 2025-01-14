import numpy as np

# Đọc dữ liệu từ file Diamonds.txt vào mảng data_diamond
# Giả sử file Diamonds.txt có dữ liệu dạng CSV hoặc tab-separated
# Cập nhật đường dẫn file nếu cần

data_diamond = np.loadtxt('Diamonds.txt', delimiter=',', skiprows=1)  # nếu dữ liệu là CSV và có header

# Hoặc nếu dữ liệu trong file là tab-separated, bạn có thể dùng delimiter='\t'
# data_diamond = np.loadtxt('Diamonds.txt', delimiter='\t', skiprows=1)

# In kích thước, số chiều, kiểu dữ liệu và số phần tử của data_diamond
print("Kích thước (shape):", data_diamond.shape)
print("Số chiều (ndim):", data_diamond.ndim)
print("Kiểu dữ liệu (dtype):", data_diamond.dtype)
print("Số phần tử (size):", data_diamond.size)
