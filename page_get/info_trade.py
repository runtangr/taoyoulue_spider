from config.conf import INFO_TRADE_LIST_URL, PROXIES, HEADER
import requests


def get_info_trade_list(page, page_num):

    data = {"parentModuleID": 5, "moduleList": "21, 72", "page": page, "pagenum": page_num}
    res = requests.post(INFO_TRADE_LIST_URL, data=data, headers=HEADER)
    if res.status_code == 200:
        return res.json()


if __name__ == "__main__":
    res = get_info_trade_list(1,1)
