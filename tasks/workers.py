import os
from datetime import timedelta
import sys
sys.path.insert(0, '..')
from celery import Celery, platforms
from config.conf import BROKER, BACKEND
from kombu import Exchange, Queue


platforms.C_FORCE_ROOT = True

tasks = [
 'tasks.news',
 'tasks.info',
 'tasks.trade_info'
]

app = Celery('ebaiyin_task', include=tasks, broker=BROKER, backend=BACKEND)


app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,

    CELERYBEAT_SCHEDULE={
        'news_task': {
            'task': 'tasks.news.execute_news',
            'schedule': timedelta(minutes=4),
            'options': {'queue': 'news', 'routing_key': 'for_news'}
        },
        'info_task': {
            'task': 'tasks.info.execute_info',
            'schedule': timedelta(minutes=3),
            'options': {'queue': 'info', 'routing_key': 'for_info'}
        },
        'trade_info_task': {
            'task': 'tasks.trade_info.execute_trade_info',
            'schedule': timedelta(minutes=3),
            'options': {'queue': 'trade_info', 'routing_key': 'for_trade_info'}
        }
    },

    CELERY_QUEUES=(
        Queue('news', exchange=Exchange('news', type='direct'),
              routing_key='for_news'),

        Queue('silver_info', exchange=Exchange('silver_info', type='direct'),
              routing_key='for_info'),
        Queue('trade_info', exchange=Exchange('trade_info', type='direct'),
              routing_key='for_trade_info'),
    )
)


