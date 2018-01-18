from utils.change import datetime2lc
import datetime
import unittest


class ChangeModel(unittest.TestCase):

    def test_datetime2lc(self):
        time_str = "2018-01-18T00:44:59"
        time = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")

        time_now = datetime.datetime.now()

        lc_date = datetime2lc(time)
        lc_date_now = datetime2lc(time_now)

        print(lc_date)
        print(lc_date_now)