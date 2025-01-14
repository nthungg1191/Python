import numpy as np

# Đọc dữ liệu từ file Diamonds.txt vào mảng data_diamond
data_diamond = np.loadtxt('Diamonds.txt', delimiter=',', skiprows=1)  # Giả sử dữ liệu là CSV và có header

# Tách mảng data_diamond thành hai vector:
# - diamond_size: Trọng lượng kim cương (Carat), nằm ở cột 0
# - diamond_price: Giá bán kim cương (Price), nằm ở cột 1
diamond_size = data_diamond[:, 0]  # Chọn tất cả các hàng, chỉ cột đầu tiên (Carat)
diamond_price = data_diamond[:, 1]  # Chọn tất cả các hàng, chỉ cột thứ hai (Price)

# In kết quả để kiểm tra
print("Trọng lượng kim cương (diamond_size):")
print(diamond_size[:10])  # In ra 10 giá trị đầu tiên

print("\nGiá bán kim cương (diamond_price):")
print(diamond_price[:10])  # In ra 10 giá trị đầu tiên
