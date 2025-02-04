import numpy as np

# Problem 1
A1 = np.array([[1, 2, 3], 
               [2, 2, 2], 
               [3, 3, 3]])
rank1 = np.linalg.matrix_rank(A1)
print("Rank of matrix A1 is:", rank1)

# Problem 2
A2 = np.array([[1, 2, 3], 
               [3, 4, 5], 
               [4, 5, 6]])
rank2 = np.linalg.matrix_rank(A2)
print("Rank of matrix A2 is:", rank2)

# Problem 3
A3 = np.array([[10, 10, 10, 10, 10], 
               [10, 10, 10, 10, 10], 
               [10, 10, 10, 10, 10], 
               [10, 10, 10, 10, 10], 
               [10, 10, 10, 10, 10]])
rank3 = np.linalg.matrix_rank(A3)
print("Rank of matrix A3 is:", rank3)
