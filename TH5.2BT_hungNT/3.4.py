import numpy as np

vector_weight = [
    96,  87, 110, 180, 139,  97, 179, 190, 167, 129,
    56, 162, 160, 122,  96, 151, 179, 167, 134, 132,
    96, 122, 166, 112,  92, 162, 152, 180, 144,  93,
    116, 160, 174, 104, 116, 191, 156, 139, 152, 128,
    149, 181, 160, 146, 129, 135, 137, 162, 158, 123,
    124, 144, 147, 187, 115, 191, 178, 166, 149, 132,
    122, 146, 127, 176, 166, 178, 161, 132, 172, 126,
    114,  94, 103, 152, 162, 115, 181, 136, 126, 141,
    123, 112, 121, 128, 138, 122, 147, 145, 125, 119,
    144, 136, 123, 113, 162, 189, 162, 181, 112, 109
]

matrix_weight = np.array(vector_weight).reshape(10, 10)

upper_no_diag = np.triu(matrix_weight, k=1)

lower_no_diag = np.tril(matrix_weight, k=-1)

print("Ma trận weight:")
print(matrix_weight, "\n")

print("Ma trận đường chéo trên (không gồm đường chéo chính):")
print(upper_no_diag)
max_upper = np.max(upper_no_diag)
print("Giá trị lớn nhất trong phần trên (không gồm chéo):", max_upper, "\n")

print("Ma trận đường chéo dưới (không gồm đường chéo chính):")
print(lower_no_diag)

max_lower = np.max(lower_no_diag)
print("Giá trị lớn nhất trong phần dưới (không gồm chéo):", max_lower)
