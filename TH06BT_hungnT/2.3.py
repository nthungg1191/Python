import pandas as pd

excel_path = '7-2/TH06BT_hungnT/movie_data.xlsx'
data = pd.read_excel(excel_path)

print(data.head())
