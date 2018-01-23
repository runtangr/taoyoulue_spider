
import datetime


def datetime2lc(time):
    utc_time = time - datetime.timedelta(hours=8)
    lc_date = {}
    time_str = datetime.datetime.strftime(utc_time,
                                          "%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    lc_date["iso"] = time_str
    lc_date["__type"] = "Date"

    return lc_date

