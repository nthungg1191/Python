import numpy as np

diem_2a = np.array([
    [5, 6, 7],  # Điểm môn 1
    [8, 5, 9],  # Điểm môn 2
    [6, 7, 8]   # Điểm môn 3
])
a = diem_2a[1,:15]

print(f"mang a ban dau: \n{a}")
print(f"So phan tu trong mang a: {a.size}")
print(f"Mang a da sap xep: {np.sort(a)}")
print(f"Gia tri trung binh mean: {np.mean(a)}")
print(f"Gia tri trung vi median: {np.median(a)}")