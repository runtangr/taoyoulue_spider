from .workers import app
from db.auMessage724 import AuMessage724
from page_parse.news_list import parse_news_list
from page_parse.content import parse_content


@app.task(ignore_result=True)
def execute_news():
    for au_message724_field in parse_news_list():
        app.send_task('tasks.news.save_news_list',
                      args=(au_message724_field,),
                      queue='news',
                      routing_key='for_news')


@app.task(ignore_result=True)
def save_news_list(au_message724_field):
    print(type(au_message724_field))
    AuMessage724.add(au_message724_field)

    app.send_task('tasks.news.save_new_content',
                  args=(au_message724_field['ArticleID'],),
                  queue='news',
                  routing_key='for_news')


@app.task(ignore_result=True)
def save_new_content(article_id):
    res_div = parse_content(article_id)

    print("article_id:", article_id)
    print("res_div:", res_div)

    AuMessage724.objects(ArticleID=article_id).update(ArticleContent=res_div)
