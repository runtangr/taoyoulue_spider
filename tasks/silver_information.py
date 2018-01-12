from .workers import app
from db.A_DxtInformation import ADxtInformation
from page_parse.information_list import parse_information_list
from page_parse.content import parse_content
import datetime


@app.task(ignore_result=True)
def execute_silver_information():
    print("start silver information crawl")
    for a_information_field in parse_information_list():

        app.send_task('tasks.silver_information.save_silver_information_list',
                      args=(a_information_field,),
                      queue='silver_information',
                      routing_key='for_silver_news')


@app.task(ignore_result=True)
def save_silver_information_list(a_information_field):
    print(type(a_information_field))
    ADxtInformation.add(a_information_field)

    app.send_task('tasks.silver_information.save_silver_information_content',
                  args=(a_information_field['information_id'],),
                  queue='silver_information',
                  routing_key='for_silver_information')


@app.task(ignore_result=True)
def save_silver_information_content(information_id):
    print("information_id:", information_id)
    res_div = parse_content(information_id)

    print("res_div:", res_div)

    ADxtInformation.objects(information_id=information_id).update(content=res_div)
