import numpy as np
a = np.random.randint(1, 33, 15)

print('Vector ban đầu:\n', a)
print('-----------------------------')
a_sort = np.sort(a)
b_sort = np.flip(a_sort)

print('Vector sắp xếp tăng dần:\n', a_sort)
print('Vector sắp xếp giảm dần:\n', b_sort)
