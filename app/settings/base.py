import os
import json

# This is the only allowed django-related package to be imported into
# our settings file.
from django.core.exceptions import ImproperlyConfigured


###### PATH CONFIGURATION
# Build paths inside the core app like this: os.path.join(APP_DIR, ...)
# Build paths inside the project app like this: os.path.join(PROJECT_DIR, ...)
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = os.path.join(APP_DIR, 'settings')
PROJECT_DIR = os.path.dirname(APP_DIR)
VAR_DIR = os.path.join(PROJECT_DIR, 'var')
RUN_DIR = os.path.join(VAR_DIR, 'run')
LOG_DIR = os.path.join(VAR_DIR, 'logs')
TMP_DIR = os.path.join(VAR_DIR, 'tmp')
SITE_NAME = '{{ project_name }}'


try:
    with open(os.path.join(SETTINGS_DIR, 'keys.json'), 'r') as fh:
        keys = json.loads(fh.read())
        fh.close()
except FileNotFoundError:
    msg = 'Configure keys.json in the settings folder'
    raise ImproperlyConfigured(msg)
except ValueError as err:
    raise err

def get_key(key, keys=keys):
    """Retrieve a configuration key value from a key dictionary or
    environment variable.

    :param key: Settings config dictionary key
    :type key: str

    :param keys: Key dictionary.
        Default: Values from keys.json as dictionary
    :type keys: dict

    :returns: Value from a key dictionary

    """
    val = keys.get(key) or os.environ.get(key)
    if not val:
        msg = (
            'Set the "{}" setting in keys.json or as environment variable.'
        ).format(key)
        raise ImproperlyConfigured(msg)
    return val


###### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_key('SECRET_KEY')
DEBUG=True


###### APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]
THIRD_PARTY_APPS = [
    'djcelery',
]
LOCAL_APPS = [
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


###### MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
DJANGO_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
THIRD_PARTY_MIDDLEWARE = [
]
LOCAL_MIDDLEWARE = [
]

MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + LOCAL_MIDDLEWARE


###### URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'app.urls'


##### SITES CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SITE_ID
SITE_ID = 1


###### TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = get_key('EMAIL_HOST_USER')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_key('EMAIL_HOST_PASSWORD')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.gmail.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 587

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[{}] '.format(SITE_NAME.upper())

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


###### WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'app.wsgi.application'


###### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = []

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


###### PASSWORD VALIDATOR CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


###### AUTHENTICATION BACKENDS CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-AUTHENTICATION_BACKENDS
# AUTHENTICATION_BACKENDS = [
# ]


###### INTERNATIONALIZATION CONFIGURATION
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


###### STATIC FILE CONFIGURATION
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(VAR_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'assets'),
]


###### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(VAR_DIR, 'media')
MEDIA_URL = '/media/'


###### LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/topics/logging/
LOG_FILE = os.path.join(LOG_DIR, '{}.log'.format(SITE_NAME))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(name)s %(pathname)s %(lineno)d - %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(module)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': 1024*1024*10,  # 10 megabytes
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'default': {
            'handlers': ['file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


###### CELERY CONFIGURATION
# See:
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#django-first-steps
# http://docs.celeryproject.org/en/latest/tutorials/daemonizing.html#generic-initd-celerybeat-django-example
import djcelery
djcelery.setup_loader()

CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

BROKER_USER = 'caffeine'
BROKER_PASS = 'changeme'
BROKER_HOST = 'rabbitmq'
BROKER_PORT = 5672
BROKER_VHOST = 'caffeine_vhost'
BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    BROKER_USER,
    BROKER_PASS,
    BROKER_HOST,
    BROKER_PORT,
    BROKER_VHOST
)
