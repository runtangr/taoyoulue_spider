from .workers import app
from db.auMessage724 import AuMessage724
from page_parse.silver.news_list import parse_news_list
from page_parse.silver.news_content import parse_news_content
import datetime


@app.task(ignore_result=True)
def execute_silver_news():
    for au_message724_field in parse_news_list():
        app.send_task('tasks.silver_news.save_silver_news_list',
                      args=(au_message724_field,),
                      queue='silver_news',
                      routing_key='for_silver_news')


@app.task(ignore_result=True)
def save_silver_news_list(au_message724_field):
    au_message724_field['LastHitTime'] = datetime.datetime.strptime(
        au_message724_field['LastHitTime'], "%Y-%m-%dT%H:%M:%S")

    au_message724_field['createdAt'] = datetime.datetime.strptime(
        au_message724_field['createdAt'], "%Y-%m-%dT%H:%M:%S.%f")

    au_message724_field['updatedAt'] = datetime.datetime.strptime(
        au_message724_field['updatedAt'], "%Y-%m-%dT%H:%M:%S.%f")

    AuMessage724.add(au_message724_field)

    app.send_task('tasks.silver_news.save_silver_new_content',
                  args=(au_message724_field['ArticleID'],),
                  queue='silver_news',
                  routing_key='for_silver_news')


@app.task(ignore_result=True)
def save_silver_new_content(article_id):
    res_div = parse_news_content(article_id)

    print("article_id:", article_id)
    print("res_div:", res_div)

    AuMessage724.objects(ArticleID=article_id).update(ArticleContent=res_div)
