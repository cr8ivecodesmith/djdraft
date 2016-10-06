from .base import *


DEBUG = False


ALLOWED_HOSTS = [
    '{{ project_name }}.dev',
]


###### APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += [
]


###### DATABASE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'caffeinedb',
        'USER': 'caffeine',
        'PASSWORD': 'changeme',
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
EMAIL_HOST = 'smtp.{{ project_name }}.dev'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 465

SERVER_EMAIL = 'errors@{{ project_name }}.dev'
DEFAULT_FROM_EMAIL = 'noreply@{{ project_name }}.dev'

###### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS += [
    ('caffeine prod', 'errors@{{ project_name }}.dev'),
]


###### CELERY CONFIGURATION
# CELERY_ROUTES = {
#     'app.tasks.example_queue': {
#         'queue': 'express_queue'
#     },
# }
