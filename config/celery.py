"""
Celery interation boilerplate
See: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

"""
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


app_env = 'config.settings.{env}'.format(
    env=os.environ.get('APP_ENV', 'prod')
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', app_env)
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
