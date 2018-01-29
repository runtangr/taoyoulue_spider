from config.conf import INFO_7X24_LIST_URL, HEADER
import requests


def get_info_7x24_list(page, page_num):
    data = {"page": page, "pagenum": page_num}
    res = requests.post(INFO_7X24_LIST_URL, data=data, headers=HEADER)
    if res.status_code == 200:
        return res.json()


if __name__ == "__main__":
    get_info_7x24_list(1, 1)

