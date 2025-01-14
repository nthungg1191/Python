import numpy as np

diem_tb = [4.8, 6.0, 4.7, 8.6, 6.2, 6.8, 5.6, 5.4, 5.9, 5.1, 7.2, 5.4, 5.9, 6.0, 7.9, 4.2, 6.1,
           6.3, 4.4, 4.7, 5.9, 5.6, 4.7, 6.4, 6.2, 6.5, 4.6, 5.8, 4.3]

print("Điểm TB của từng học sinh trong lớp:")
print(diem_tb)

diem_cao_nhat = max(diem_tb)
hoc_sinh_cao = diem_tb.index(diem_cao_nhat)
print("\nĐiểm TB cao nhất:", diem_cao_nhat)
print("Của học sinh thứ:", hoc_sinh_cao + 1)

diem_day_du_cao = [7, 10, 9, 8, 7, 10, 10, 8, 9, 8]
print("Bảng điểm đầy đủ của học sinh:", diem_day_du_cao)

diem_thap_nhat = min(diem_tb)
hoc_sinh_thap = diem_tb.index(diem_thap_nhat)
print("\nĐiểm TB thấp nhất:", diem_thap_nhat)
print("Của học sinh thứ:", hoc_sinh_thap + 1)

diem_day_du_thap = [3, 2, 2, 1, 2, 6, 2, 7, 9, 8]
print("Bảng điểm đầy đủ của học sinh:", diem_day_du_thap)