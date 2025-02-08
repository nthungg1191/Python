from sklearn.datasets import load_diabetes, load_digits

# Tải dữ liệu diabetes cho bài toán hồi quy
diabetes = load_diabetes()
diabetes_data, diabetes_target = diabetes.data, diabetes.target

# Tải dữ liệu digits cho bài toán phân loại
digits = load_digits()
digits_data, digits_target = digits.data, digits.target

# Hiển thị thông tin về các bộ dữ liệu
datasets_info = [
    {"name": "Diabetes", "shape": diabetes_data.shape, "description": diabetes.DESCR},
    {"name": "Digits", "shape": digits_data.shape, "description": digits.DESCR}
]

for dataset in datasets_info:
    print(f"Dataset Name: {dataset['name']}")
    print(f"Shape: {dataset['shape']}")
    print("Description:")
    print(dataset['description'])
    print("\n" + "-"*80 + "\n")
