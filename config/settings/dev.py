# flake8: noqa
from .base import *


DEBUG = True


###### APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += [
    'django_extensions',
]


###### CACHE CONFIGURATION
# https://docs.djangoproject.com/en/1.11/ref/settings/#caches
# https://docs.djangoproject.com/en/1.11/topics/cache/#django-s-cache-framework
# https://docs.djangoproject.com/en/1.11/topics/cache/#cache-arguments
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


###### LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING['handlers']['file']['level'] = 'DEBUG'

LOGGING['loggers']['django.request']['handlers'] += ['console', 'file']
LOGGING['loggers']['django.request']['level'] = 'DEBUG'

LOGGING['loggers']['default']['handlers'] += ['console']
LOGGING['loggers']['default']['level'] = 'DEBUG'
