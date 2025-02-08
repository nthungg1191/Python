import requests
import pandas as pd

# URL của API
url = "http://api.plos.org/search?q=title:VIRUS"

# Gửi yêu cầu tới API
response = requests.get(url)
data = response.json()

# Lấy danh sách các bài báo
articles = data['response']['docs']

# Tạo danh sách để lưu trữ dữ liệu
articles_list = []

# Lấy thông tin cần thiết từ mỗi bài báo và lưu trữ vào danh sách
for article in articles:
    article_info = {
        'id': article.get('id', None),
        'eissn': article.get('eissn', None),
        'author_display': ", ".join(article.get('author_display', [])),
        'abstract': article.get('abstract', [None])[0],
        'title_display': article.get('title_display', None),
        'score': article.get('score', None)
    }
    articles_list.append(article_info)

# Chuyển đổi danh sách thành DataFrame
df = pd.DataFrame(articles_list)

# Lưu DataFrame vào file CSV
df.to_csv('Paper.csv', index=False)

print("Dữ liệu đã được lưu vào file Paper.csv")
