from datetime import datetime

from mongoengine import *
from db.init_database import r_A_DxtInformation


class ADxtInformation(Document):

    title = StringField()
    source = StringField(default='')
    sourceUrl = StringField(default='')
    summary = StringField(default='')
    thumbnail = StringField(default='')
    content = StringField(default='')
    categories = ListField(default=[])
    tags = ListField(default=[])
    teacher = DictField(default={})
    nature = StringField(default='')
    publishTime = StringField(default='')
    clickNumber = IntField(default=0)
    likeNumber = IntField(default=0)
    shareNumber = IntField(default=0)
    collectNumber = IntField(default=0)
    AttachFile = StringField(default='')
    isDisable = IntField(default=0)

    pushTime = StringField(default='')
    isPushed = StringField(default='')
    createdAt = StringField()
    updatedAt = StringField()
    information_id = IntField(default=0)

    isTop = BooleanField(default=False)
    isHot = BooleanField(default=False)
    isRecommend = BooleanField(default=False)

    meta = {
        'collection': 'A_DxtInformation',
        'indexes': ['information_id']
    }

    @classmethod
    def add(cls, a_information_field):
        item = cls.get(a_information_field['information_id'])
        if not item:
            item = cls(**a_information_field)
            item.save()
        return item

    @classmethod
    def get(cls, information_id):
        rs = r_A_DxtInformation.get(information_id)
        if rs:
            return cls.from_json(rs)
        try:
            item = cls.objects(information_id=information_id).first()
        except DoesNotExist:
            pass
        else:
            if item:
                r_A_DxtInformation.set(information_id, item.to_json())
                return item