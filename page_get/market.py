from config.conf import MARKET_URL, HEADER
import requests
import random


def get_market_list():

    res = requests.get(MARKET_URL.format(random.random()),
                       headers=HEADER)
    if res.status_code == 200:
        # print(res.text)
        data_list = res.text.split('[')[1].split(',')

        for res_data in data_list:
            data_str = res_data.split('"')[1]
            detail_data = data_str.split("#")
            yield detail_data


if __name__ == "__main__":
    for data in get_market_list():
        print(data)
