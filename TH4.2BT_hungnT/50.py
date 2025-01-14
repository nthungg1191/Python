import numpy as np

diem_tb_mon = [4.73, 4.43, 5.5, 4.83, 4.97, 5.6, 6.23, 7.3, 6.13, 7.97]

print("Điểm TB của từng môn học:")
print(diem_tb_mon)

diem_cao_nhat = max(diem_tb_mon)
mon_cao_nhat = diem_tb_mon.index(diem_cao_nhat)
print("\nĐiểm TB cao nhất của môn học:", diem_cao_nhat)
print("Môn học thứ:", mon_cao_nhat + 1)

diem_day_du_cao = [7, 8, 7, 8, 6, 10, 10, 6, 8, 10, 8, 9, 8, 8, 5, 10, 8, 7, 8, 7, 9, 9, 8, 7, 7, 7, 10, 8, 9, 7]
print("Bảng điểm đầy đủ của môn học:", diem_day_du_cao)

diem_thap_nhat = min(diem_tb_mon)
mon_thap_nhat = diem_tb_mon.index(diem_thap_nhat)
print("\nĐiểm TB thấp nhất của môn học:", diem_thap_nhat)
print("Môn học thứ:", mon_thap_nhat + 1)

diem_day_du_thap = [3, 5, 3, 10, 9, 1, 9, 8, 3, 1, 6, 0, 7, 10, 8, 5, 2, 7, 7, 1, 1, 6, 1, 6, 3, 0, 2, 2, 1, 6]
print("Bảng điểm đầy đủ của môn học:", diem_day_du_thap)