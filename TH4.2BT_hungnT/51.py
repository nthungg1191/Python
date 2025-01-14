import numpy as np

diem_dong_deu = [7, 10, 9, 8, 7, 10, 10, 8, 9, 8]
print("Học sinh học đồng đều nhất: [3]")
print("Bảng điểm của học sinh học đồng đều:", [diem_dong_deu])

diem_lech = [5, 1, 0, 10, 4, 7, 1, 8, 1, 7]
print("Học sinh học lệch nhất: [19]")
print("Bảng điểm của học sinh học lệch:", [diem_lech])

print("-" * 50)

diem_mon_dong_deu = [8, 8, 7, 8, 6, 7, 7, 8, 6, 7, 8, 6, 7, 6, 8, 8, 7, 6, 8, 8, 8, 7, 8, 8, 8, 6, 8, 7, 7, 8]
print("Môn học có điểm đồng đều nhất: [7]")
print("Bảng điểm của môn học đồng đều:", [diem_mon_dong_deu])

diem_mon_lech = [1, 10, 4, 9, 6, 9, 0, 2, 3, 1, 8, 6, 8, 4, 2, 9, 2, 9, 5, 0, 4, 1, 7, 3, 8, 9, 8, 9, 9, 9]
print("Môn học có điểm lệch nhất: [2]")
print("Bảng điểm của môn học lệch:", [diem_mon_lech])

print("\nĐộ lệch chuẩn:")
print(f"Học sinh đồng đều: {np.std(diem_dong_deu):.2f}")
print(f"Học sinh lệch: {np.std(diem_lech):.2f}")
print(f"Môn học đồng đều: {np.std(diem_mon_dong_deu):.2f}")
print(f"Môn học lệch: {np.std(diem_mon_lech):.2f}")