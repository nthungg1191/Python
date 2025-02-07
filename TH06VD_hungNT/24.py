import pandas as pd 
path_excel = r'7-2/TH06VD_hungNT/Book1.xlsx'
data_ex = pd.read_excel(path_excel,sheet_name=4080130_02,skiprows=9)
data_ex.info()