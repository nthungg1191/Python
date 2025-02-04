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

vector_diagonal = np.diag(matrix_weight)
print("Vector_diagonal chứa các phần tử trên đường chéo chính của ma trận weight:")
print(vector_diagonal)

trace_weight = np.trace(matrix_weight)
print("Trace của ma trận weight:", trace_weight)
