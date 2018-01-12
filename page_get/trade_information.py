from config.conf import TRADE_INFORMATION_LIST_URL, NEWS_CONTENT_URL, PROXIES, HEADER
import requests


def get_trade_information_list(page, page_num):

    data = {"parentModuleID": 5, "moduleList": "21, 72", "page": page, "pagenum": page_num}
    res = requests.post(TRADE_INFORMATION_LIST_URL, data=data, headers=HEADER, proxies=PROXIES)
    if res.status_code == 200:
        return res.json()


def get_trade_information_content(article_id):

    res = requests.post(NEWS_CONTENT_URL.format(article_id), headers=HEADER, proxies=PROXIES)
    if res.status_code == 200:
        return res.json()

if __name__ == "__main__":
    res = get_trade_information_list(1,1)
    get_trade_information_content(33401)