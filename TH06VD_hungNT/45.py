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
