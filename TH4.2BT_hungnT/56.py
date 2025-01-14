import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data from table 1 (Square Feet vs Price)
data1 = {
    'square_feet': [1460, 2108, 1743, 1403, 1864, 2291, 1977, 1610, 1536, 1792, 1821, 2216],
    'price': [238700, 309300, 301900, 297100, 302400, 314900, 336400, 297000, 282400, 293200, 304300, 311700]
}

# Data from table 2 (Distance vs Price)
data2 = {
    'distance': [2.6, 0.8, 1.0, 0.6, 1.5, 2.0, 3.4, 1.2, 3.6, 1.7],
    'price': [214, 376, 280, 302, 200, 190, 236, 244, 128, 165]
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Calculate correlation coefficients
corr1 = stats.pearsonr(df1['square_feet'], df1['price'])
corr2 = stats.pearsonr(df2['distance'], df2['price'])

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Plot 1: Square Feet vs Price
ax1.scatter(df1['square_feet'], df1['price'], color='blue')
ax1.set_xlabel('Square Feet')
ax1.set_ylabel('Price')
ax1.set_title('Square Feet vs Price')

# Plot 2: Distance vs Price
ax2.scatter(df2['distance'], df2['price'], color='blue')
ax2.set_xlabel('Distance from City Center (miles)')
ax2.set_ylabel('Price (x $1000)')
ax2.set_title('Distance vs Price')

plt.tight_layout()

# Print correlation results
print("Phân tích kết quả:\n")
print("1. Mối quan hệ giữa Diện tích và Giá bán:")
print(f"   - Hệ số tương quan Pearson: {corr1[0]:.4f}")
print(f"   - P-value: {corr1[1]:.4f}")
if corr1[0] > 0:
    print("   - Có mối tương quan dương: khi diện tích tăng, giá bán có xu hướng tăng")
else:
    print("   - Có mối tương quan âm: khi diện tích tăng, giá bán có xu hướng giảm")
print(f"   - Mức độ tương quan: {abs(corr1[0]):.2%}")

print("\n2. Mối quan hệ giữa Khoảng cách và Giá bán:")
print(f"   - Hệ số tương quan Pearson: {corr2[0]:.4f}")
print(f"   - P-value: {corr2[1]:.4f}")
if corr2[0] > 0:
    print("   - Có mối tương quan dương: khi khoảng cách tăng, giá bán có xu hướng tăng")
else:
    print("   - Có mối tương quan âm: khi khoảng cách tăng, giá bán có xu hướng giảm")
print(f"   - Mức độ tương quan: {abs(corr2[0]):.2%}")

plt.show()