import numpy as np
from scipy import stats

# Create sample data arrays for each subject
diem_2a = [
    [1, 1, 1, 1, 1, 1],  # Môn 0
    [1, 1, 1, 1, 1, 1],  # Môn 1
    [9, 9, 9, 9, 9, 9, 9, 8],  # Môn 2
    [6, 6, 6, 6, 6],  # Môn 3
    [4, 4, 4, 4, 4, 4],  # Môn 4
    [5, 5, 5, 5, 5],  # Môn 5
    [9, 9, 9, 9, 9, 9, 9, 9],  # Môn 6
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],  # Môn 7
    [8, 8, 8, 8, 8, 8, 8],  # Môn 8
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]  # Môn 9
]

# Calculate mode for each subject
for i in range(len(diem_2a)):
    a = stats.mode(diem_2a[i])
    print(f'Môn {i}: Điểm xuất hiện nhiều nhất: {a[0]}, số lần: {a[1]}')

# Print the type of result
print(type(a))