categories = ["Thiếu cân ", "Cân đối", "Thừa cân", "Béo phì", "Béo phì nguy hiểm"]
values = [10, 13, 16, 14, 47]

total_people = sum(values)

print("BMI Statistics:")
for category, value in zip(categories, values):
    percentage = (value / total_people) * 100
    print(f"{category}: {value} người ({percentage:.2f}%)")

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=['brown', 'pink', 'blue', 'yellow', 'orange'])
plt.title("BMI Classification Distribution")
plt.xlabel("BMI Categories")
plt.ylabel("Number of People")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
