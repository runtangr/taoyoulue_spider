from .workers import app
from config.conf import HUA_TONG_URL, MAX_SEARCH_PAGE_NUM, MAX_SEARCH_PAGE
from page_get.silver import news_list
from db.auMessage724 import AuMessage724
import json


@app.task(ignore_result=True)
def save_news():
    for page in xrange(1, MAX_SEARCH_PAGE):

        res_dict = news_list.get_news_list(page, MAX_SEARCH_PAGE_NUM)

        if res_dict['Status'] == 200:
            au_message724_field = dict()
            for data in res_dict['Data']:
                au_message724_field['LastHitTime'] = data['publishtime']
                au_message724_field['ArticleID'] = data['id']
                au_message724_field['title'] = data['title']

                AuMessage724.add(au_message724_field)
        else:
            raise ValueError
