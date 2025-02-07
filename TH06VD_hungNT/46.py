# Kết nối tới CSDL Mongo
import pymongo as mg

# Thiết lập Tham số tới server CSDL
address='118.70.196.130:27017'
user='root'
pas='Hung@1234'
auth='SCRAM-SHA-1'
database = 'Data_Laichau'
coll_name='LC_Meteorology'
#---------------------------------
# Thực hiện kết nối tới CSDL
client = mg.MongoClient(address,username=user,password=pas,authMechanism=auth)
db=client[database] # truy cập đến CSDL: Data_Laichau
col = db[coll_name] # truy cập đến collection: LC_Meteorology

# Thực hiện truy vấn lấy dữ liệu
# Thiết lập câu truy vấn thực hiện:
# 1. Lấy dữ liệu từ trạm có mã TU
# 2. Sắp xếp dữ liệu theo thứ tự thời gian giảm dần
stationid = 'TU'
data_mg = col.find({"Id":stationid}).sort([('Time',-1)])
print(type(data_mg))
# Khởi tạo các biến list để lưu trữ dữ liệu
df_time, df_rain, df_t2m, df_tm, df_tx = [], [], [], [], []

# Lặp qua dữ liệu ban đầu và thêm vào các list tương ứng
for i in data_mg:
    df_time.append(str(i['Time']))
    df_rain.append(i['Rain'])
    df_t2m.append(i['T2m'])
    df_tm.append(i['Tm'])
    df_tx.append(i['Tx'])

# Kết hợp các list lại thành một list các tuple
ziplist_water = list(zip(df_time, df_rain, df_t2m, df_tm, df_tx))

# Chuyển đổi list các tuple thành DataFrame
import pandas as pd
df = pd.DataFrame(ziplist_water, columns=['Time', 'Rain', 'T2m', 'Tm', 'Tx'])

# Hiển thị thông tin về DataFrame
df.info()

# Hiển thị 5 dòng dữ liệu đầu tiên của DataFrame
print(df.head())