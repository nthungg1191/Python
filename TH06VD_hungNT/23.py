import pandas as pd 
path_excel = r'7-2/TH06VD_hungNT/Book1.xlsx'
data_ex = pd.read_excel(path_excel,sheet_name=0,usecols=[1,6,7,8,9,10],
                        index_col=0)
data_ex.info()
data_ex.head()