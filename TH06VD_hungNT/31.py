import pandas as pd 
path_json = r'7-2/TH06VD_hungNT/data_product.json'

data_json = pd.read_json(path_json)
print(data_json)