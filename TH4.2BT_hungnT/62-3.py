# Dữ liệu nhiệt độ của 6 thành phố (nhiệt độ cao nhất, thấp nhất trong một ngày)
city_temperatures = {
    "Hà Nội": [32, 28, 30, 29, 31, 30],
    "Hồ Chí Minh": [35, 32, 34, 33, 35, 34],
    "Đà Nẵng": [33, 30, 32, 31, 33, 32],
    "Cần Thơ": [34, 31, 32, 33, 34, 33],
    "Nha Trang": [30, 28, 29, 30, 31, 29],
    "Hải Phòng": [28, 26, 27, 28, 29, 27]
}

# Hàm tính toán nhiệt độ cao nhất, thấp nhất và trung bình cho mỗi thành phố
def calculate_city_temperatures(city, temps):
    max_temp = max(temps)  # Nhiệt độ cao nhất của thành phố
    min_temp = min(temps)  # Nhiệt độ thấp nhất của thành phố
    avg_temp = sum(temps) / len(temps)  # Nhiệt độ trung bình của thành phố
    return max_temp, min_temp, avg_temp

# Tính toán và hiển thị nhiệt độ cho từng thành phố
for city, temps in city_temperatures.items():
    max_temp, min_temp, avg_temp = calculate_city_temperatures(city, temps)
    print(f"{city}:")
    print(f"  Nhiệt độ cao nhất (Max): {max_temp}°C")
    print(f"  Nhiệt độ thấp nhất (Min): {min_temp}°C")
    print(f"  Nhiệt độ trung bình (Avg): {avg_temp:.2f}°C")
    print("-" * 40)  # Dòng phân cách giữa các thành phố
