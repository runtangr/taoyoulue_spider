from page_get.market import get_market_list
from utils.change import datetime2lc
import datetime
import time
import os
from page_parse.qiniu_deal import save2qiniu


def parse_market_list():
    time.sleep(10)
    for data_list in get_market_list():
        db_data = {}

        if len(data_list) < 12:
            continue

        db_data['type'] = int(data_list[0])
        db_data['createdAt'] = \
            datetime.datetime.utcnow().isoformat()[:-3] + 'Z'
        db_data['updatedAt'] = \
            datetime.datetime.utcnow().isoformat()[:-3] + 'Z'

        if db_data['type'] == 0:
            db_data['star'] = int(data_list[1])
            db_data['pushTime'] = data_list[2]
            db_data['minContent'] = data_list[3]
            db_data['url'] = data_list[4]

            if 'jin10' in db_data['url']:
                db_data['url'] = ''

            db_data['img'] = data_list[6]
            if len(db_data['img']) != 0:

                img = parse_img_url(db_data['img'].split('_')[0] + '.png')
                db_data['img'] = img

            db_data['timeStr'] = data_list[11]

        elif db_data['type'] == 1:

            db_data['time_show'] = data_list[1]
            db_data['minContent'] = data_list[2]
            db_data['previous'] = data_list[3]
            db_data['consensus'] = data_list[4]
            db_data['actual'] = data_list[5]
            db_data['star'] = int(data_list[6])
            db_data['status_name'] = data_list[7]
            db_data['pushTime'] = data_list[8]
            db_data['country'] = data_list[9]
            db_data['datanameId'] = int(data_list[11])
            db_data['timeStr'] = data_list[12]

        if "金十" in db_data['minContent']:
            continue

        push_time = datetime2lc(datetime.datetime.strptime(
            db_data['pushTime'], "%Y-%m-%d %H:%M:%S"))
        db_data['pushTime'] = push_time

        yield db_data


def parse_img_url(image_url):
    # save qiniu
    key = os.path.join("market", image_url)
    save2qiniu(key, os.path.join("http://image.jin10.com", image_url))
    # deal img url
    return os.path.join("http://cdn.re-media.cn", key)

if __name__ == "__main__":
    for res_data in parse_market_list():
        print(res_data)
