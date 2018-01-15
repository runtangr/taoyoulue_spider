from config.conf import NEWS_LIST_URL, HEADER, NEWS_CONTENT_URL
import requests


def get_news_list(page, page_num):
    data = {"page": page, "pagenum": page_num}
    res = requests.post(NEWS_LIST_URL, data=data, headers=HEADER)
    if res.status_code == 200:
        return res.json()


def get_news_content(article_id):

    res = requests.get(NEWS_CONTENT_URL.format(
        str(article_id)), headers=HEADER)
    return res

if __name__ == "__main__":
    get_news_list(1, 1)
    div_str = get_news_content(32702)
