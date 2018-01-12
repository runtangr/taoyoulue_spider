# coding=utf-8

from config.conf import NEWS_CONTENT_URL, HEADER, PROXIES
import requests


def get_news_content(article_id):

    res = requests.get(NEWS_CONTENT_URL.format(
        str(article_id)), headers=HEADER, proxies=PROXIES)
    return res


if __name__ == "__main__":

    # 32786:not img article  32702:have img article
    div_str = get_news_content(32702)

