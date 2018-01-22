from page_get.trade_info import get_trade_info_list
import time
from .qiniu_deal import save2qiniu
import os
import re
import datetime
from utils.change import datetime2lc


def parse_trade_info_list():
    res_dict = get_trade_info_list(1, 1)
    time.sleep(10)
    if res_dict['Status'] == 200:
        a_information_field = dict()
        for data in res_dict['Data']:
            a_information_field['title'] = data['InformationTitle']
            a_information_field['source'] = data['SourceType']
            a_information_field['sourceUrl'] = data['SourceUrl']
            a_information_field['summary'] = data['Introduction']
            image_url = parse_img_url(data['ImageUrl'])
            a_information_field['thumbnail'] = image_url
            a_information_field['content'] = ''  # div
            a_information_field['categories'] = ['行业新闻']
            a_information_field['tags'] = []
            a_information_field['teacher'] = {}
            a_information_field['nature'] = ''

            lc_create_time = datetime2lc(datetime.datetime.strptime(
                data['UpdateTime'], "%Y-%m-%d %H:%M:%S"))
            a_information_field['publishTime'] = lc_create_time
            a_information_field['clickNumber'] = 0
            a_information_field['likeNumber'] = 0
            a_information_field['shareNumber'] = 0
            a_information_field['collectNumber'] = 0
            a_information_field['AttachFile'] = ''
            a_information_field['isDisable'] = 0

            a_information_field['information_id'] = data['Id']

            a_information_field['createdAt'] = \
                datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
            a_information_field['updatedAt'] = \
                datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'

            yield a_information_field


def parse_img_url(image_url):
    # save qiniu
    img_list = re.split('/', image_url)
    key = os.path.join(img_list[-3], img_list[-2], img_list[-1])
    save2qiniu(key, image_url)
    # deal img url
    return os.path.join("http://cdn.re-media.cn", key)


if __name__ == "__main__":
    parse_trade_info_list()
