from .workers import app
from db.A_DxtInformation import ADxtInformation
from page_parse.trade_info_list import parse_trade_info_list
from page_parse.content import parse_content


@app.task(ignore_result=True)
def execute_trade_info():
    print("start silver trade information crawl")
    for a_information_field in parse_trade_info_list():

        app.send_task('tasks.trade_info.save_trade_info_list',
                      args=(a_information_field,),
                      queue='trade_info',
                      routing_key='for_trade_info')


@app.task(ignore_result=True)
def save_trade_info_list(a_information_field):
    print(type(a_information_field))
    ADxtInformation.add(a_information_field)

    app.send_task('tasks.trade_info.save_trade_info_content',
                  args=(a_information_field['information_id'],),
                  queue='trade_info',
                  routing_key='for_trade_info')


@app.task(ignore_result=True)
def save_trade_info_content(information_id):
    print("trade_info_id:", information_id)
    res_div = parse_content(information_id)

    print("res_div:", res_div)

    ADxtInformation.objects(information_id=information_id).update(
        content=res_div)
