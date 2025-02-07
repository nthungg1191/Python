import pandas as pd

# Đường dẫn tới tệp CSV
path = r'7-2/TH06VD_hungNT/dataahihihi.csv'
data = pd.read_csv(path, nrows=100,usecols=['Height_cm','Weight_kg'])
data.info()
print(data.head())
