# Dữ liệu nhiệt độ của 6 thành phố (nhiệt độ cao nhất, thấp nhất trong một ngày)
city_temperatures = {
    "Hà Nội": [32, 28, 30, 29, 31, 30],
    "Hồ Chí Minh": [35, 32, 34, 33, 35, 34],
    "Đà Nẵng": [33, 30, 32, 31, 33, 32],
    "Cần Thơ": [34, 31, 32, 33, 34, 33],
    "Nha Trang": [30, 28, 29, 30, 31, 29],
    "Hải Phòng": [28, 26, 27, 28, 29, 27]
}

# Hàm tính toán nhiệt độ cao nhất, thấp nhất và trung bình của 6 thành phố
def calculate_temperatures(temps):
    all_temps = []

    # Lấy tất cả các nhiệt độ của các thành phố vào một danh sách chung
    for city, temp_list in temps.items():
        all_temps.extend(temp_list)

    max_temp = max(all_temps)  # Nhiệt độ cao nhất
    min_temp = min(all_temps)  # Nhiệt độ thấp nhất
    avg_temp = sum(all_temps) / len(all_temps)  # Nhiệt độ trung bình

    return max_temp, min_temp, avg_temp

# Tính toán nhiệt độ
max_temp, min_temp, avg_temp = calculate_temperatures(city_temperatures)

# In kết quả
print(f"Nhiệt độ cao nhất (Max): {max_temp}°C")
print(f"Nhiệt độ thấp nhất (Min): {min_temp}°C")
print(f"Nhiệt độ trung bình (Avg): {avg_temp:.2f}°C")
