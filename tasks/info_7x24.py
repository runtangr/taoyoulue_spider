from .workers import app
from db.auMessage724 import AuMessage724
from page_parse.info_7x24_list import parse_info_7x24_list
from page_parse.info_content import parse_content
from logger import crawler


@app.task(ignore_result=True)
def execute_info_7x24():
    crawler.info('The info_7x24 task is starting...')
    for au_message724_field in parse_info_7x24_list():
        app.send_task('tasks.info_7x24.save_info_7x24_list',
                      args=(au_message724_field,),
                      queue='info_7x24',
                      routing_key='for_info_7x24')


@app.task(ignore_result=True)
def save_info_7x24_list(au_message724_field):
    crawler.info('The info_7x24 list task is starting...')
    AuMessage724.add(au_message724_field)

    app.send_task('tasks.info_7x24.save_info_7x24_content',
                  args=(au_message724_field['ArticleID'],),
                  queue='info_7x24',
                  routing_key='for_info_7x24')


@app.task(ignore_result=True)
def save_info_7x24_content(article_id):
    crawler.info('The info_7x24 content task is starting...')
    crawler.info('The info_7x24 content article id is :{}'.format(article_id))
    res_div = parse_content(article_id)
    crawler.info('The info_7x24 content is :{}...'.format(res_div[:20]))

    AuMessage724.objects(ArticleID=article_id).update(ArticleContent=res_div)
