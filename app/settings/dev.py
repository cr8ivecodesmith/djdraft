from .base import *


DEBUG = True


###### APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += [
    'django_extensions',
]


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'caffeinedb',
        'USER': 'caffeine',
        'PASSWORD': 'c@ff3in3Ov3rl0ad',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = get_key('EMAIL_HOST_USER')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_key('EMAIL_HOST_PASSWORD')


###### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ('codehappy dev', get_key('EMAIL_HOST_USER')),
]


###### LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/1.9/topics/logging/
LOGGING['handlers']['file']['level'] = 'DEBUG'

LOGGING['loggers']['django.request']['handlers'] += ['console', 'file']
LOGGING['loggers']['django.request']['level'] = 'DEBUG'

LOGGING['loggers']['default']['handlers'] += ['console']
LOGGING['loggers']['default']['level'] = 'DEBUG'
