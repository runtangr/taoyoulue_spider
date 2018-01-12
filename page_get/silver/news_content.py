# coding=utf-8

from config.conf import NEWS_CONTENT_URL
import requests
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
          'Host':'www.ebaiyin.com'
          }
proxies = {
        "http": "http://"+'127.0.0.1:8087',
        "https": "http://"+'127.0.0.1:8087',
	}

def get_news_content(article_id):

    res = requests.get(NEWS_CONTENT_URL.format(article_id), headers=header, proxies=proxies)
    return res


if __name__ == "__main__":

    # 32786 wu  32702 you
    div_str = get_news_content(32702)

