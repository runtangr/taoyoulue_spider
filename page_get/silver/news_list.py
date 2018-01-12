from config.conf import NEWS_LIST_URL
import requests

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
          'Host':'www.ebaiyin.com'
          }
proxies = {
        "http": "http://"+'127.0.0.1:8087',
        "https": "http://"+'127.0.0.1:8087',
	}


def get_news_list(page, page_num):
    data = {"page": page, "pagenum": page_num}
    res = requests.post(NEWS_LIST_URL, data=data, headers=header, proxies=proxies)
    if res.status_code == 200:
        return res.json()


if __name__ == "__main__":
    get_news_list(1, 1)