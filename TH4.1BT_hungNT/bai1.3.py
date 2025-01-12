import numpy as np

n = int(input("Nhập giá trị n (số nguyên dương): "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
else:
    matrix = np.random.randint(0, 101, size=(n, n), dtype=np.int32)
    print("Ma trận được tạo:")
    print(matrix)

    x = int(input("Nhập vào giá trị x (0-100): "))
    if x < 0 or x > 100:
        print("Vui lòng nhập giá trị trong khoảng từ 0 đến 100.")
    else:
        count_equal = np.sum(matrix == x)      
        count_less = np.sum(matrix < x)        
        count_greater = np.sum(matrix > x)    

        print(f"Số phần tử có giá trị bằng {x} trong ma trận: {count_equal}")
        print(f"Số phần tử nhỏ hơn giá trị {x} trong ma trận: {count_less}")
        print(f"Số phần tử lớn hơn giá trị {x} trong ma trận: {count_greater}")
