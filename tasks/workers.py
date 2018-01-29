import os
from datetime import timedelta
import sys
sys.path.insert(0, '..')
from celery import Celery, platforms
from config.conf import BROKER, BACKEND
from kombu import Exchange, Queue


platforms.C_FORCE_ROOT = True

tasks = [
 'tasks.info_7x24',
 'tasks.info',
 'tasks.info_trade'
]

app = Celery('taoyoulue_task', include=tasks, broker=BROKER, backend=BACKEND)


app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,

    CELERYBEAT_SCHEDULE={
        'info_7x24_task': {
            'task': 'tasks.info_7x24.execute_info_7x24',
            'schedule': timedelta(minutes=4),
            'options': {'queue': 'info_7x24', 'routing_key': 'for_info_7x24'}
        },
        'info_task': {
            'task': 'tasks.info.execute_info',
            'schedule': timedelta(minutes=3),
            'options': {'queue': 'info', 'routing_key': 'for_info'}
        },
        'info_trade_task': {
            'task': 'tasks.info_trade.execute_info_trade',
            'schedule': timedelta(minutes=3),
            'options': {'queue': 'info_trade', 'routing_key': 'for_info_trade'}
        }
    },

    CELERY_QUEUES=(
        Queue('info_7x24', exchange=Exchange('info_7x24', type='direct'),
              routing_key='for_info_7x24'),

        Queue('info', exchange=Exchange('info', type='direct'),
              routing_key='for_info'),
        Queue('info_trade', exchange=Exchange('info_trade', type='direct'),
              routing_key='for_info_trade'),
    )
)


