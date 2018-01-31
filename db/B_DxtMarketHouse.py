from mongoengine import *
from db.init_database import r_B_DxtMarketHouse


class BDxtMarketHouse(Document):
    type = IntField()
    star = IntField()
    pushTime = DictField(default={})
    minContent = StringField(default='')
    url = StringField(default='')
    img = StringField(default='')
    time_show = StringField(default='')
    country = StringField(default='')
    previous = StringField(default='')
    consensus = StringField(default='')
    actual = StringField(default='')
    status_name = StringField(default='')
    datanameId = IntField(default=0)
    timeStr = StringField(default='')
    channelSource = StringField(default='')
    isDisable = IntField(default=0)

    meta = {
        'collection': 'B_DxtMarketHouse',
        'indexes': ['timeStr']
    }

    @classmethod
    def add(cls, b_market_field):
        item = cls.get(b_market_field['timeStr'])

        if not item:
            item = cls(**b_market_field)
            item.save()
        return item

    @classmethod
    def get(cls, b_market_timestr):
        rs = r_B_DxtMarketHouse.get(b_market_timestr)
        if rs:
            return cls.from_json(rs)
        try:
            item = cls.objects(timeStr=b_market_timestr).first()
        except DoesNotExist:
            pass
        else:
            if item:
                r_B_DxtMarketHouse.set(b_market_timestr, item.to_json())
                return item

