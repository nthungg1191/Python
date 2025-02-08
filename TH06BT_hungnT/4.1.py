from pymongo import MongoClient
import pandas as pd

# Kết nối đến MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['LC_Meteorology']

# Truy vấn dữ liệu
query = {"Id": "LC"}
projection = {"Time": 1, "Rain": 1, "T2m": 1, "_id": 0}
data = list(collection.find(query, projection).sort("Time", -1).limit(1000))

# Chuyển đổi dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Lưu dữ liệu vào file CSV
df.to_csv('LC_Meteorology.csv', index=False)

print("Dữ liệu đã được lưu vào file LC_Meteorology.csv")
