import numpy as np 
import random
n = int(input("Nhap vao 1 so nguyen n: "))

if n <= 0:
    print("Nhap lai 1 so nguyen khac lon hon 0! ")
else:
    matrix = np.random.randint(0,100, size = (n,n), dtype=np.int32 )
    print("Ma tran: ")
    print(matrix)
    print(f"Kieu dữ liệu của phần tử trong ma trận: {matrix.dtype}")
    print(f"Kich thuoc cua mang ma tran: {matrix.shape}")
    print(f"So phan tu cua mang ma tran: {matrix.size}")
    print(f"So chieu cua mang ma tran: {matrix.ndim}")
    v_chinh = matrix.diagonal()
    v_phu = matrix[:,::-1].diagonal()
    print(f"Vector cac phan tu nam tren duong cheo chinh: {v_chinh}")
    print(f"Vector cac phan tu nam tren duong cheo phu: {v_phu}")