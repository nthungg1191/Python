import numpy as np
x = np.array([17, 2, 11, 1, 9, 15, 1, 3, 8, 1, 12, 13, 5])

t1 = np.where(x==1)
print(t1)
print('Số phần tử thỏa mãn điều kiện = 1: ', t1[0].size)
print('---------------------------------------------')

t2 = np.where(x>10)
print(t2)
print('Số phần tử thỏa mãn điều kiện >10: ', t2[0].size)
print('---------------------------------------------')

t3 = np.where((x>=5) & (x<=12))
print(t3)
print('Số phần tử thỏa mãn điều kiện [5, 12]: ', t3[0].size)
