from .base import *


DEBUG = False


ALLOWED_HOSTS = [
    'abm-can.codehappylabs.com',
]


###### APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += [
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
# See: https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = get_key('EMAIL_HOST_USER')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_key('EMAIL_HOST_PASSWORD')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.zoho.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 465

SERVER_EMAIL = 'errors@codehappy.ph'
DEFAULT_FROM_EMAIL = 'noreply@codehappy.ph'

###### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ('ABM CAN Errors', 'errors@codehappy.ph'),
]


###### CELERY CONFIGURATION
# CELERY_ROUTES = {
#     'scrapers.tasks.update_diffbot_prices': {
#         'queue': 'dbot_update'
#     },
# }
