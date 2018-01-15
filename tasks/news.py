from .workers import app
from db.auMessage724 import AuMessage724
from page_parse.news_list import parse_news_list
from page_parse.content import parse_content
from logger import crawler


@app.task(ignore_result=True)
def execute_news():
    crawler.info('The news task is starting...')
    for au_message724_field in parse_news_list():
        app.send_task('tasks.news.save_news_list',
                      args=(au_message724_field,),
                      queue='news',
                      routing_key='for_news')


@app.task(ignore_result=True)
def save_news_list(au_message724_field):
    crawler.info('The news list task is starting...')
    AuMessage724.add(au_message724_field)

    app.send_task('tasks.news.save_new_content',
                  args=(au_message724_field['ArticleID'],),
                  queue='news',
                  routing_key='for_news')


@app.task(ignore_result=True)
def save_new_content(article_id):
    crawler.info('The news content task is starting...')
    crawler.info('The news content article id is :{}'.format(article_id))
    res_div = parse_content(article_id)
    crawler.info('The news content is :{}...'.format(res_div[:10]))

    AuMessage724.objects(ArticleID=article_id).update(ArticleContent=res_div)
