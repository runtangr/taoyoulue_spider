
from config.conf import INFO_CONTENT_URL, PROXIES, HEADER
import requests


def get_info_content(article_id):

    res = requests.get(INFO_CONTENT_URL.format(
        str(article_id)), headers=HEADER)
    return res
