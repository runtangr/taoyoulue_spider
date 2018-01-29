from config.conf import INFO_LIST_URL, PROXIES, HEADER
import requests


def get_info_list(page, page_num):
    data = {"parentModuleID": 4,
            "moduleList": "10, 44, 45, 46, 47",
            "page": page, "pagenum": page_num}
    res = requests.post(INFO_LIST_URL, data=data, headers=HEADER)
    if res.status_code == 200:
        return res.json()


if __name__ == "__main__":
    res_dict = get_info_list(1, 1)

