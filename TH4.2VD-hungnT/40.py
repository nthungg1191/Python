import numpy as np

diem_2a = np.array([5, 2, 9, 5, 8, 7, 6, 8])  

print(f"Điểm cao nhất lớp: {max(diem_2a)}")
print(f"Điểm thấp nhất lớp: {min(diem_2a)}")

diem_2a_2d = np.array([
    [5, 6, 7],  # Điểm môn 1
    [8, 5, 9],  # Điểm môn 2
    [6, 7, 8]   # Điểm môn 3
])

for i in range(diem_2a_2d.shape[0]): 
    print(f"Môn {i+1}: Điểm max là {np.max(diem_2a_2d[i, :])}")
    print(f"Môn {i+1}: Điểm min là {np.min(diem_2a_2d[i, :])}")

for i in range(diem_2a_2d.shape[1]): 
    print(f"Học sinh {i+1}: Điểm max là {np.max(diem_2a_2d[:, i])}")
    print(f"Học sinh {i+1}: Điểm min là {np.min(diem_2a_2d[:, i])}")
