import numpy as np 
vector_a = np.array([5,7,2,9,10,15,2,9,2,17,28,16],dtype = np.int16)
print(vector_a)
print(f"So phan tu cua vector: {vector_a.size}")

matrix_a = vector_a.reshape((3,4))
print(f'Reshape ve matrix: 3 x 4')
print(matrix_a)
print(f"So pahn tu cua matrix_a {matrix_a.size}")
maxtrix_b = vector_a.reshape((2,6))
print(f"Reshape ve matrix 2 x 6: \n{maxtrix_b}")
