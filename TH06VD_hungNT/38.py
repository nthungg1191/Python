import pandas as pd 
import requests as rq
url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9 '
result_money = rq.get(url_api)
print(result_money.status_code)

data_text = result_money.text
data_json = result_money.json()
print(f"text: {result_money}")
print('------------------')
print(f'Json: {data_json}')