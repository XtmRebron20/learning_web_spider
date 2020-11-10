import requests
import re
import json

def get_on_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/86.0.4240.183 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None
def parse_one_page(html,offset):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="'
        '(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>'
        '(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', 
        re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items: # 返回的是一个可迭代对象！！！不可以直接使用，需要用for语句循环解析！！！
        yield {        
            'index':str(int(item[0]) + offset),
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(items[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(items[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open('my_first_webspider_project/results.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offest=' + str(offset)
    html = get_on_page(url)
    # print(html)
    results = parse_one_page(html,offset)
    for result in results:
        write_to_file(result)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)