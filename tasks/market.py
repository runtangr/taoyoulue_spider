from .workers import app
from db.B_DxtMarketHouse import BDxtMarketHouse
from page_parse.market import parse_market_list
from logger import crawler


@app.task(ignore_result=True)
def execute_market():
    crawler.info('The market task is starting...')
    for b_market_field in parse_market_list():

        app.send_task('tasks.market.save_market',
                      args=(b_market_field,),
                      queue='market',
                      routing_key='for_market')


@app.task(ignore_result=True)
def save_market(b_market_field):
    crawler.info('The save market task is starting...')
    BDxtMarketHouse.add(b_market_field)


