# Tạo file Data_BMI.txt và tính BMI

# Bước 1: Tạo file Data_BMI.txt chứa thông tin chiều cao và cân nặng của 100 người
import random

# Tạo dữ liệu ngẫu nhiên cho 100 người
with open("Data_BMI.txt", "w") as file:
    for _ in range(100):
        height = random.randint(150, 200)  # Chiều cao ngẫu nhiên trong khoảng 150-200 cm
        weight = random.randint(50, 100)  # Cân nặng ngẫu nhiên trong khoảng 50-100 kg
        file.write(f"{height} {weight}\n")

print("File Data_BMI.txt đã được tạo thành công.")

# Bước 2: Đọc file Data_BMI.txt, tính BMI và phân loại
# BMI = weight (kg) / (height (m))^2
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese"
    else:
        return "Extremely Obese"

# Đọc file và tính toán
bmi_results = []
with open("Data_BMI.txt", "r") as file:
    for line in file:
        height, weight = map(int, line.split())
        bmi = calculate_bmi(height, weight)
        category = classify_bmi(bmi)
        bmi_results.append((height, weight, round(bmi, 2), category))

# Ghi kết quả ra file mới
with open("BMI_Results.txt", "w") as file:
    file.write("Height(cm) Weight(kg) BMI Category\n")
    for result in bmi_results:
        file.write(f"{result[0]} {result[1]} {result[2]} {result[3]}\n")

print("Kết quả BMI đã được lưu vào file BMI_Results.txt.")
