from datetime import datetime

from mongoengine import *
from .init_database import r_auMessage724

class AuMessage724(Document):
    LastHitTime = StringField()
    ArticleID = IntField()
    title = StringField()
    isArticle = IntField(default=0)
    ArticleContent = StringField(default='')
    source = StringField(default='')
    pushTime = StringField(default='')
    isPushed = StringField(default='')

    meta = {
        'collection': 'auMessage724',
        'indexes': ['ArticleID']
    }

    @classmethod
    def add(cls, au_message724_field):
        item = cls.get(au_message724_field['ArticleID'])
        if not item:

            item = cls(**au_message724_field)
            item.save()
        return item

    @classmethod
    def get(cls, article_id):
        rs = r_auMessage724.get(article_id)
        if rs:
            return cls.from_json(rs)
        try:
            item = cls.objects(ArticleID=article_id).first()
        except DoesNotExist:
            pass
        else:
            if item:
                r_auMessage724.set(article_id, item.to_json())
                return item