import pandas as pd 

path = r'7-2/TH06BT_hungnT/json_data.json'

data_json = pd.read_json(path, encoding='utf-8-sig')
print(data_json)