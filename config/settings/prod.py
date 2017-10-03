# flake8: noqa
from .base import *


DEBUG = False


###### HOSTS CONFIGURATION
# https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_config('DJANGO_APP_ALLOWED_HOSTS', [
    '0.0.0.0'
])


###### DATABASE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_config('PGSQL_DATABASE', 'caffeinedb'),
        'USER': get_config('PGSQL_USER', 'caffeine'),
        'PASSWORD': get_config('PGSQL_PASS', 'changeme'),
        'HOST': 'postgres',
        'PORT': 5432,
    }
}


###### CACHE CONFIGURATION
# https://docs.djangoproject.com/en/1.11/ref/settings/#caches
# https://docs.djangoproject.com/en/1.11/topics/cache/#django-s-cache-framework
# https://docs.djangoproject.com/en/1.11/topics/cache/#cache-arguments
# LOCATION value refer to memcached service name in docker-compose file
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
        'TIMEOUT': 300,
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
            'server_max_value_length': 2097152,
        },
    }
}
