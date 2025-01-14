import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dữ liệu mẫu (có thể thay thế bằng dữ liệu thực từ file)
weights = np.array([0.2, 0.3, 0.5, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.8, 3.0, 3.5, 4.0])
prices = np.array([1000, 2000, 3500, 5000, 6500, 8000, 10000, 11500, 12500, 13500, 14000, 14500, 15000, 15500, 17000])

# Tính hệ số tương quan
correlation = np.corrcoef(weights, prices)[0, 1]

# Tạo biểu đồ
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.scatter(weights, prices, color='blue')

# Đặt tiêu đề và nhãn
plt.title('BIỂU ĐỒ THỂ HIỆN MỐI TƯƠNG QUAN GIỮA TRỌNG LƯỢNG (CARAT) VÀ GIÁ BÁN KIM CƯƠNG ($)')
plt.xlabel('Trọng lượng (Carat)')
plt.ylabel('Giá bán ($)')

# Thiết lập giới hạn trục x và y
plt.xlim(0, max(weights) + 0.5)
plt.ylim(0, max(prices) + 1000)

# In hệ số tương quan
print(f"Hệ số tương quan giữa trọng lượng và giá bán kim cương: {correlation}")

plt.show()