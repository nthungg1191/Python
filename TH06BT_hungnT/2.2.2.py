import pandas as pd

# Đọc dữ liệu từ file CSV
file_path = '7-2/TH06BT_hungnT/loan_data_full.csv'
data = pd.read_csv(file_path)

# Chia dữ liệu thành hai DataFrame
df_number = data.select_dtypes(include=['number'])
df_object = data.select_dtypes(include=['object'])

# Hiển thị 5 dòng dữ liệu đầu tiên của df_number
print("Dữ liệu số:")
print(df_number.head())

# Hiển thị 5 dòng dữ liệu đầu tiên của df_object
print("Dữ liệu chuỗi:")
print(df_object.head())
