import pandas as pd

# Đường dẫn tới tệp CSV
path = r'7-2/TH06VD_hungNT/dataahihihi.csv'

data = pd.read_csv(path,names=['ID','Sex','H(cm)','W(kg)'],skiprows=5)
data.info()
print(data.head())