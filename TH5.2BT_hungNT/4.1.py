import numpy as np

# 1. Tạo vector_height và vector_weight (mỗi cái 100 phần tử)
vector_height = [174, 189, 155, 129, 160, 154, 174, 169, 174, 169,
                 154, 125, 170, 151, 137, 161, 149, 177, 153, 128,
                 177, 173, 152, 143, 165, 155, 140, 168, 144, 157,
                 153, 144, 179, 125, 135, 178, 154, 155, 133, 147,
                 150, 124, 152, 144, 140, 122, 128, 126, 135, 155,
                 144, 149, 169, 144, 152, 141, 160, 178, 147, 166,
                 153, 173, 139, 161, 132, 177, 159, 189, 154, 167,
                 177, 140, 158, 155, 125, 166, 138, 155, 181, 155,
                 153, 164, 148, 189, 152, 178, 153, 128, 159, 177,
                 153, 174, 121, 148, 181, 187, 163, 140, 149, 189]

vector_weight = [96,  87, 110, 180, 139,  97, 179, 190, 167, 129,
                 56, 162, 160, 122,  96, 151, 179, 167, 134, 132,
                 96, 122, 166, 112,  92, 162, 152, 180, 144,  93,
                 116, 160, 174, 104, 116, 191, 156, 139, 152, 128,
                 149, 181, 160, 146, 129, 135, 137, 162, 158, 123,
                 124, 144, 147, 187, 115, 191, 178, 166, 149, 132,
                 122, 146, 127, 176, 166, 178, 161, 132, 172, 126,
                 114,  94, 103, 152, 162, 115, 181, 136, 126, 141,
                 123, 112, 121, 128, 138, 122, 147, 145, 125, 119,
                 144, 136, 123, 113, 162, 189, 162, 181, 112, 109]

# 2. Chuyển về ma trận 10×10
height = np.array(vector_height).reshape(10, 10)
weight = np.array(vector_weight).reshape(10, 10)

# In ra để kiểm tra
print("Ma trận height:")
print(height, "\n")

print("Ma trận weight:")
print(weight, "\n")

# 3. So sánh (ví dụ: height > weight, element-wise)
compare_matrix = (height > weight)
print("Ma trận so sánh (height > weight):")
print(compare_matrix, "\n")

# 4. Cộng
sum_matrix = height + weight
print("Ma trận cộng (height + weight):")
print(sum_matrix, "\n")

# 5. Trừ
diff_matrix = height - weight
print("Ma trận trừ (height - weight):")
print(diff_matrix, "\n")

# 6. Nhân
# a) Element-wise multiplication
elemwise_mul = height * weight
print("Ma trận nhân từng phần tử (height * weight):")
print(elemwise_mul, "\n")

# b) Matrix multiplication (theo quy tắc nhân ma trận)
matmul_result = height @ weight
print("Ma trận nhân ma trận (height @ weight):")
print(matmul_result)
