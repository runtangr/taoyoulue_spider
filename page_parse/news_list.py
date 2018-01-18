from config.conf import MAX_SEARCH_PAGE_NUM, MAX_SEARCH_PAGE, DATE_LENGTH
from page_get.news import get_news_list
import datetime
import time
from utils.change import datetime2lc


def parse_news_list():

    res_dict = get_news_list(1, 1)
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

            lc__time_now = datetime2lc(datetime.datetime.now())
            au_message724_field['createdAt'] = lc__time_now
            au_message724_field['updatedAt'] = lc__time_now

            yield au_message724_field

    else:
        raise ValueError

if __name__ == "__main__":
    for i in parse_news_list():
        pass
