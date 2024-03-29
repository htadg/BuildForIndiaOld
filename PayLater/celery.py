from __future__ import absolute_import, unicode_literals
import os

from django.conf import settings

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PayLater.settings')

app = Celery('PayLater')

# Using a string here means the worker doesn't have to serialize
# the configuration object.
app.config_from_object('django.conf:settings')

# load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))