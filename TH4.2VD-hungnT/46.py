import numpy as np

# Tạo dữ liệu điểm cho các học sinh
diem_2a = [
    [8, 10, 9, 7, 16, 15],  # Học sinh 0
    [9, 8, 10, 15, 16],     # Học sinh 1
    [7, 8, 9, 15],          # Học sinh 2
    [6, 7, 8, 9],           # Học sinh 3
    [8, 9, 10, 15],         # Học sinh 4
    [7, 8, 9, 16],          # Học sinh 5
    [6, 8, 9, 16],          # Học sinh 6
    [8, 9, 10, 15],         # Học sinh 7
    [7, 8, 9, 13],          # Học sinh 8
    [8, 9, 10, 17],         # Học sinh 9
    [7, 8, 9, 14]           # Học sinh 10
]

# Tính range (độ chênh lệch) cho từng học sinh
for i in range(len(diem_2a)):
    print(f'Độ chênh điểm của học sinh {i}: ',
        diem_2a[i][np.argmax(diem_2a[i])] - diem_2a[i][np.argmin(diem_2a[i])])