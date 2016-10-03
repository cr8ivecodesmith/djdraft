#!/bin/bash

DJANGO_SETTINGS=app.settings.$APP_ENV
DJANGO_WSGI=app.wsgi
SOCKFILE=$PROJECT_APP_DIR/var/run/gunicorn.sock
PIDFILE=$PROJECT_APP_DIR/var/run/gunicorn.pid
LOG_FILE=$PROJECT_APP_DIR/var/logs/gunicorn.log
LOG_LEVEL=info
NUM_WORKERS=2

# Delete any existing sock and pid files
rm -f $PIDFILE $SOCKFILE

echo "-> Starting gunicorn"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS
export PYTHONPATH=$PROJECT_APP_DIR:$PYTHONPATH

. $PROJECT_APP_VENV/bin/activate
cd $PROJECT_APP_DIR
exec gunicorn \
    ${DJANGO_WSGI}:application \
    --name project \
    --user caffeine \
    --group caffeine \
    --workers $NUM_WORKERS \
    --bind=unix:$SOCKFILE \
    --log-level=$LOG_LEVEL \
    --log-file=$LOG_FILE \
    --pid=$PIDFILE \
    -D
