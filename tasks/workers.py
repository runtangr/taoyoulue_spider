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
]

app = Celery('ebaiyin_task', include=tasks, broker=BROKER, backend=BACKEND)


app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,

    CELERYBEAT_SCHEDULE={
        'silver_news_task': {
            'task': 'tasks.silver_news.save_news',
            'schedule': timedelta(seconds=20),
            'options': {'queue': 'silver_news', 'routing_key': 'for_silver_news'}
        }
    },

    CELERY_QUEUES=(
    Queue('silver_news', exchange=Exchange('silver_news', type='direct'), routing_key='for_silver_news'),
    )
)


