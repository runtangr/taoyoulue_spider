from config.conf import MAX_SEARCH_PAGE_NUM, MAX_SEARCH_PAGE, DATE_LENGTH
from page_get.news import get_news_list
import datetime
import time


def parse_news_list():

    res_dict = get_news_list(1, 1)
    time.sleep(10)
    if res_dict['Status'] == 200:
        au_message724_field = dict()
        for data in res_dict['Data']:
            publish_time = datetime.datetime.strptime(data['publishtime'],
                                                      "%Y/%m/%d %H:%M:%S")
            au_message724_field['LastHitTime'] = publish_time
            au_message724_field['ArticleID'] = data['id']
            if len(str(data['id'])) != DATE_LENGTH:
                au_message724_field['isArticle'] = 1
            au_message724_field['title'] = data['title']
            au_message724_field['createdAt'] = datetime.datetime.now()
            au_message724_field['updatedAt'] = datetime.datetime.now()

            yield au_message724_field

    else:
        raise ValueError

if __name__ == "__main__":
    for i in parse_news_list():
        pass
