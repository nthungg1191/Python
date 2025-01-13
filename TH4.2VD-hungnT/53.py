import numpy as np
import matplotlib.pyplot as plt

a_giohoc = np.array([1, 4, 7, 1, 2, 8, 0, 3, 8, 6])

b_diem = np.array([7, 7, 9, 3, 4, 9, 0, 5, 10, 8])

co = np.corrcoef(a_giohoc, b_diem)
print('Type of correlation coefficient:')
print(type(co))
print('\nHệ số tương quan:')
print(co)

plt.figure(figsize=(10, 6))
plt.scatter(a_giohoc, b_diem, color='blue')
plt.grid(True)
plt.xlabel('Giờ học bài (tuần)')
plt.ylabel('Điểm môn học')
plt.title('Mối tương quan giữa giờ học bài và điểm thi')
plt.xlim(0, 9)
plt.ylim(0, 11)
plt.show()