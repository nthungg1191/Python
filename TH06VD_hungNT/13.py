import pandas as pd

# Đường dẫn tới tệp CSV
path = '7-2\TH06VD_hungNT\dataahihihi.csv'

# Sử dụng phương thức read_csv để đọc dữ liệu từ tệp CSV
data = pd.read_csv(path)

# Hiển thị thông tin của DataFrame
data.info()

data1 = pd.read_csv(path,index_col=5)
data1.info()
data1.head()