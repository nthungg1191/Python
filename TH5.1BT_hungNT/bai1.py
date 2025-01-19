import numpy as np 
vector_a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                     16, 17, 18, 19, 20 ,21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

print(vector_a)

a_le = vector_a[vector_a%2 != 0]
a_chan = vector_a[vector_a%2 == 0]
a_3 = vector_a[vector_a%3 == 0]
print(f"Vector a_le: {a_le}")
print(f"Vector a_chan: {a_chan}")
print(f"Vector a_3: {a_3}")
