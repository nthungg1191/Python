import pandas as pd
from sklearn.datasets import load_wine

# Tải bộ dữ liệu về rượu vang
wine_data = load_wine()

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)
df['target'] = wine_data.target

# Chuyển dữ liệu thành ndarray
ndarray_data = wine_data.data

# Hiển thị 5 mẫu đầu tiên từ DataFrame
print("Dữ liệu dưới dạng DataFrame:")
print(df.head())

# Hiển thị 5 mẫu đầu tiên từ ndarray
print("\nDữ liệu dưới dạng ndarray:")
print(ndarray_data[:5])
