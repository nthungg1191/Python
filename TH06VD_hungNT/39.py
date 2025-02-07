import requests as rq
import pandas as pd

# URL API để lấy tỷ giá
url_api = 'https://api.exchangerate-api.com/v4/latest/USD'

# Truyền tham số cho url
# Lấy tỷ giá của một số ngoại tệ: GBP, JPY, MYR, THB, KRW, VND
result_money1 = rq.get(url_api, params={'symbols': 'USD, JPY, THB, VND, MYR, GBP, KRW'})
data_json1 = result_money1.json()

# Tạo DataFrame từ dữ liệu JSON
df1 = pd.DataFrame(data_json1)

# Hiển thị 10 hàng đầu tiên của DataFrame
print(df1.head(10))
