import numpy as np

diem_2a = np.array([
    [5, 6, 7],  # Điểm môn 1
    [8, 5, 9],  # Điểm môn 2
    [6, 7, 8]   # Điểm môn 3
])
print(f"Diem trung binh cua ca lop 2a: {np.mean(diem_2a)}")

for i in range(0,diem_2a.shape[1]):
    print(f"Diem trung binh cua hoc sinh {i} : {np.mean(diem_2a[:,i])}")