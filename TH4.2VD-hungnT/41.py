import numpy as np

diem_2a = np.array([
    [5, 6, 7],  # Điểm môn 1
    [8, 5, 9],  # Điểm môn 2
    [6, 7, 8]   # Điểm môn 3
])
print('Tong tat ca cac diem trong cua lop 2a: ',np.sum(diem_2a))

for i in range(0,diem_2a.shape[1]):
    print(f"Tong diem cac mon cua hoc sinh {i} : {np.sum(diem_2a[:,i])}")