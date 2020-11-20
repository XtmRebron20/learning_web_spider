import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
res = requests.get(url, headers=headers)
print(res.status_code) # 400响应？
html = res.text
doc = pq(html)
# print(doc)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('./learning_save_data/explore.txt', 'a', encoding='utf-8') # 也可以使用with open语句
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 +'\n')
    file.close()

