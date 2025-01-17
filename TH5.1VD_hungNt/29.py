import numpy as np
arr = np.array([(1, 2, 3, 4, 5, 4, 4), 
                (7, 3, 4, 8, 9, 6, 7)])

x = np.where(arr > 4)

print('Ma trận A:\n', arr)
print('-------------------------------')
print(x)
print('Số phần tử thỏa mãn điều kiện > 4:', x[0].size)
