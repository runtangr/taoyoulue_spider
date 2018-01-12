import os
from datetime import timedelta
import sys
sys.path.insert(0, '..')
from celery import Celery, platforms
from config.conf import BROKER, BACKEND
from kombu import Exchange, Queue


platforms.C_FORCE_ROOT = True

tasks = [
 'tasks.silver_news',
 'tasks.silver_information',
 'tasks.silver_trade_information'
]

app = Celery('ebaiyin_task', include=tasks, broker=BROKER, backend=BACKEND)


app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,

    CELERYBEAT_SCHEDULE={
        'silver_news_task': {
            'task': 'tasks.silver_news.execute_silver_news',
            'schedule': timedelta(minutes=4),
            'options': {'queue': 'silver_news', 'routing_key': 'for_silver_news'}
        },
        'silver_information_task': {
            'task': 'tasks.silver_information.execute_silver_information',
            'schedule': timedelta(minutes=3),
            'options': {'queue': 'silver_information', 'routing_key': 'for_silver_information'}
        },
        'silver_trade_information_task': {
            'task': 'tasks.silver_trade_information.execute_silver_trade_information',
            'schedule': timedelta(minutes=3),
            'options': {'queue': 'silver_trade_information', 'routing_key': 'for_silver_trade_information'}
        }
    },

    CELERY_QUEUES=(
        Queue('silver_news', exchange=Exchange('silver_news', type='direct'), routing_key='for_silver_news'),

        Queue('silver_information', exchange=Exchange('silver_information', type='direct'),
              routing_key='for_silver_information'),
        Queue('silver_trade_information', exchange=Exchange('silver_trade_information', type='direct'),
              routing_key='for_silver_trade_information'),
    )
)


