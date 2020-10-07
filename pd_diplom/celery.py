import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pd_diplom.settings')

celery_app = Celery('pd_diplom')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

