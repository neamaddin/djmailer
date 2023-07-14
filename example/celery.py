import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

app = Celery('example')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(packages=['djmailer', ])
