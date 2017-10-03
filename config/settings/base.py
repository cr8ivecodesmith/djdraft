# flake8: noqa
import os
import json

###### PATH CONFIGURATION
# Build paths inside the core app like this: os.path.join(CONFIG_DIR, ...)
# Build paths inside the project app like this: os.path.join(PROJECT_DIR, ...)
CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(CONFIG_DIR)
VAR_DIR = os.path.join(PROJECT_DIR, 'var')

SITE_NAME = '{{ project_name }}'


_config = {}
try:
    with open(os.path.join(VAR_DIR, 'etc', 'config.json')) as fh:
        _config = json.loads(fh.read())
except Exception as err:
    print(err)


def get_config(key, default=None, config=_config):
    """
    .. py::function get_config(key[, default, keys])

    Retrieve a configuration key value from a config dictionary or
    environment variable.

    :param str key: Name of the configuration to get
    :param default: Set a default value
    :param dict config:
        Config dictionary.
        Default: Values from config.json as dictionary

    :return: Config value

    """
    val = (
        config.get(key, default) or
        os.environ.get(key, default=default) or
        default
    )
    return val


###### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_config('DJANGO_APP_SECRET_KEY', '{{ secret_key }}')
DEBUG = get_config('DJANGO_APP_DEBUG', False)


###### HOSTS CONFIGURATION
# https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_config('DJANGO_APP_ALLOWED_HOSTS', [
    'localhost',
    '127.0.0.1',
    '0.0.0.0'
])


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
    'django_celery_results',
    'django_celery_beat',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
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
ROOT_URLCONF = 'config.urls'


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
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


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


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST_USER = get_config('DJANGO_APP_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = get_config('DJANGO_APP_EMAIL_HOST_PASSWORD', '')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_SUBJECT_PREFIX = '[{site_name}] {env} - '.format(
    site_name=SITE_NAME.upper(),
    env=get_config('APP_ENV', 'prod').upper()
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


###### WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'


###### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    (
        '{app_user} {site_name}'.format(
            app_user=get_config('APP_USER', 'caffeine').title(),
            site_name=SITE_NAME.title()
        ),
        EMAIL_HOST_USER
    ),
]

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

LANGUAGE_CODE = get_config('DJANGO_APP_LANGUAGE_CODE', 'en-us')
TIME_ZONE = get_config('DJANGO_APP_TIME_ZONE', 'UTC')
USE_I18N = True
USE_L10N = True
USE_TZ = True


###### STATIC FILE CONFIGURATION
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(VAR_DIR, 'share', 'static')
STATICFILES_DIRS = [
    os.path.join(VAR_DIR, 'share', 'assets'),
]


###### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(VAR_DIR, 'share', 'media')
MEDIA_URL = '/media/'


###### LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/topics/logging/
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
            'filename': os.path.join(
                VAR_DIR, 'log',
                '{}.log'.format(SITE_NAME.lower())
            ),
            'maxBytes': 1024 * 1024 * 10,  # 10 megabytes
            'backupCount': 5,
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


###### REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '100/minute'
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}


###### CELERY CONFIGURATION
# See:
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#django-first-steps
# http://docs.celeryproject.org/en/latest/tutorials/daemonizing.html#generic-initd-celerybeat-django-example
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BROKER_URL = 'amqp://{user}:{pass}@{host}:{port}/{vhost}'.format(
    user=get_config('RABBITMQ_DEFAULT_USER', 'caffeine'),
    pass=get_config('RABBITMQ_DEFAULT_PASS', 'chang3m3'),
    host='rabbitmq',
    port=5672,
    vhost=get_config('RABBITMQ_DEFAULT_VHOST', 'caffeine_vhost')
)
