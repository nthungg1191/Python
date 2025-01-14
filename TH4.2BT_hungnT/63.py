# Dữ liệu nhiệt độ của 6 thành phố (nhiệt độ cao nhất, thấp nhất trong một ngày)
city_temperatures = {
    "Hà Nội": [32, 28, 30, 29, 31, 30],
    "Hồ Chí Minh": [35, 32, 34, 33, 35, 34],
    "Đà Nẵng": [33, 30, 32, 31, 33, 32],
    "Cần Thơ": [34, 31, 32, 33, 34, 33],
    "Nha Trang": [30, 28, 29, 30, 31, 29],
    "Hải Phòng": [28, 26, 27, 28, 29, 27]
}

# Hàm tính toán các giá trị Max, Min, và Mean cho mỗi thành phố
def calculate_city_temperatures(temps):
    max_temp = max(temps)  # Nhiệt độ cao nhất của thành phố
    min_temp = min(temps)  # Nhiệt độ thấp nhất của thành phố
    avg_temp = sum(temps) / len(temps)  # Nhiệt độ trung bình của thành phố
    return max_temp, min_temp, avg_temp

# Tạo ma trận data_thongke (3 hàng x 7 cột)
data_thongke = []

# Các giá trị riêng biệt cho từng thành phố
max_values = []
min_values = []
avg_values = []

# Tính toán các giá trị cho từng thành phố
for city, temps in city_temperatures.items():
    max_temp, min_temp, avg_temp = calculate_city_temperatures(temps)
    max_values.append(max_temp)
    min_values.append(min_temp)
    avg_values.append(round(avg_temp, 2))

# Thống kê chung (cho tất cả các thành phố)
all_temps = []
for temps in city_temperatures.values():
    all_temps.extend(temps)

max_all = max(all_temps)
min_all = min(all_temps)
avg_all = round(sum(all_temps) / len(all_temps), 2)

# Thêm giá trị thống kê chung vào cuối mỗi danh sách
max_values.append(max_all)
min_values.append(min_all)
avg_values.append(avg_all)

# Tạo ma trận data_thongke với 3 hàng, 7 cột
data_thongke.append(max_values)
data_thongke.append(avg_values)
data_thongke.append(min_values)

# Lưu ma trận vào file thongke.txt
with open("thongke.txt", "w") as f:
    # Ghi dữ liệu vào file, mỗi hàng sẽ được ghi vào một dòng
    for row in data_thongke:
        f.write("\t".join(map(str, row)) + "\n")

# In kết quả ra màn hình (dành cho người dùng tham khảo)
for row in data_thongke:
    print("\t".join(map(str, row)))
