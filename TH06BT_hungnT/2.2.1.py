import pandas as pd

# Đọc dữ liệu từ file CSV với các tham số mặc định
file_path = '7-2/TH06BT_hungnT/loan_data_full.csv'
data = pd.read_csv(file_path)

# Hiển thị 5 hàng đầu tiên của dữ liệu
print(data.head())
