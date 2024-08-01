"""
init celery instance
"""
from celery import Celery

from app.config import settings


celery_app = Celery(settings.SERVICE_NAME)
celery_app.conf.broker_url = str(settings.CELERY_BROKER_URL)
celery_app.conf.result_backend = str(settings.CELERY_RESULT_BACKEND)
celery_app.conf.broker_connection_retry_on_startup = True

celery_app.conf.task_routes = {
    'app.services.celery.tasks.example.example_task': {
        'queue': 'example_queue'
    },
}

# this task works every 60 second
celery_app.conf.beat_schedule = {
    'example_beat': {
        'task': "app.services.celery.tasks.example.example_task",
        'schedule': 60,  # sec
        'args': ('Dima', )
    },
}
