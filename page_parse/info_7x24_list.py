from config.conf import DATE_LENGTH
from page_get.info_7x24 import get_info_7x24_list
import datetime
import time
from utils.change import datetime2lc


def parse_info_7x24_list():

    res_dict = get_info_7x24_list(1, 1)
    time.sleep(10)
    if res_dict['Status'] == 200:
        au_message724_field = dict()
        for data in res_dict['Data']:
            publish_time = datetime.datetime.strptime(data['publishtime'],
                                                      "%Y/%m/%d %H:%M:%S")
            lc_publish_time = datetime2lc(publish_time)
            au_message724_field['LastHitTime'] = lc_publish_time
            au_message724_field['ArticleID'] = data['id']
            if len(str(data['id'])) != DATE_LENGTH:
                au_message724_field['isArticle'] = 1
            au_message724_field['title'] = data['title']

            au_message724_field['createdAt'] = \
                datetime.datetime.utcnow().isoformat()[:-3] + 'Z'
            au_message724_field['updatedAt'] = \
                datetime.datetime.utcnow().isoformat()[:-3] + 'Z'

            yield au_message724_field

    else:
        raise ValueError

if __name__ == "__main__":
    for i in parse_info_7x24_list():
        pass
