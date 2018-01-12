from config.conf import NEWS_LIST_URL, HEADER, PROXIES
import requests



def get_news_list(page, page_num):
    data = {"page": page, "pagenum": page_num}
    res = requests.post(NEWS_LIST_URL, data=data, headers=HEADER, proxies=PROXIES)
    if res.status_code == 200:
        return res.json()


if __name__ == "__main__":
    get_news_list(1, 1)