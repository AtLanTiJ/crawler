import requests
from bs4 import BeautifulSoup
import threading


# 优先深度策略
# 爬虫函数，定义爬取深度为n
def crawler(n, url):
    if n < 1:
        return 0

    # 获取html源码
    resp = requests.get(url)
    _html = BeautifulSoup(resp.text, 'html5lib')

    # 去除字符串中非法字符，方便作为文件名
    s_link = url.lstrip('https://')
    illegal_s = ['/', '\\', '*', '.', '<', '>', ':', '"', '?', '|', ' ']
    for _str in illegal_s:
        s_link = s_link.replace(f'{_str}', '-')

    links = _html.find_all('a')
    except_link = ["https://beian.miit.gov.cn/"]
    # 从源码中解析其他url
    for link in links:

        # 排除部分网页
        if link['href'] in except_link:
            continue

        # 写入文件
        filename = f'{N - n + 1}层(' + s_link + ').txt'
        with open(f'./links/{filename}', mode='a') as file:
            file.write(link['href'])
            file.write('\n')

        i = 1
        # 最多执行5个线程
        if i < 6:
            # 递归调用爬虫函数
            th = threading.Thread(target=crawler, args=(n - 1, url + link['href'])).start()
            i += i
        else:
            # 等待已创建的5个线程执行完毕
            th.join()
            i = 1

    print(f'{N - n + 1}层线程执行完毕！')
    return 1


if __name__ == '__main__':
    url = input('url:')
    global N
    N = int(input('爬取深度：'))
    crawler(N, url)
