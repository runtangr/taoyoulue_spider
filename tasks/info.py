from .workers import app
from db.A_DxtInformation import ADxtInformation
from page_parse.info_list import parse_info_list
from page_parse.content import parse_content
from logger import crawler


@app.task(ignore_result=True)
def execute_info():
    crawler.info('The info task is starting...')
    for a_information_field in parse_info_list():

        app.send_task('tasks.info.save_info_list',
                      args=(a_information_field,),
                      queue='info',
                      routing_key='for_info')


@app.task(ignore_result=True)
def save_info_list(a_information_field):
    crawler.info('The info list task is starting...')
    ADxtInformation.add(a_information_field)

    app.send_task('tasks.info.save_info_content',
                  args=(a_information_field['information_id'],),
                  queue='info',
                  routing_key='for_info')


@app.task(ignore_result=True)
def save_info_content(information_id):
    crawler.info('The info content task is starting...')
    crawler.info('The info content info id is :{}'.format(information_id))
    res_div = parse_content(information_id)

    crawler.info('The info content is :{}...'.format(res_div[:20]))

    ADxtInformation.objects(information_id=information_id).update(content=res_div)
