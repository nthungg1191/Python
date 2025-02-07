import json 
with open(path_json,'r') as myfile:
    data=myfile.read()
path_json = r'7-2/TH06VD_hungNT/data_product.json'
obj = json.loads(data)
type(obj)