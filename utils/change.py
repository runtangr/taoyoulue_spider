
import datetime


def datetime2lc(time):
    lc_date = {}
    time_str = datetime.datetime.strftime(time, "%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'

    lc_date["__type"] = "Date"
    lc_date["iso"] = time_str

    return lc_date

