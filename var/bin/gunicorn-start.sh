#!/bin/bash

## SCRIPT PATH SETTINGS
PID=$$
SCRIPT=$(basename $0)
FILENAME="${SCRIPT%.*}"
SCRIPT_PATH=$(readlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT_PATH)
VAR_DIR=$(dirname $SCRIPT_DIR)
APP_DIR=$(dirname $VAR_DIR)


## MAIN
DJANGO_SETTINGS=config.settings.$APP_ENV
DJANGO_WSGI=config.wsgi
SOCK_FILE=$APP_PROJECT_ROOT/var/run/gunicorn.sock
PID_FILE=$APP_PROJECT_ROOT/var/run/gunicorn.pid
LOG_FILE=$APP_PROJECT_ROOT/var/log/gunicorn.log
LOG_LEVEL=info
NUM_WORKERS=4
NUM_THREADS=4
TIMEOUT=180

# Delete any existing sock and pid files
if [ -f $PID_FILE ];then
    echo "-> Stopping webservice"
    (cat $PID_FILE | xargs kill -15) || echo "" && rm -f $PID_FILE
fi

if [ -f $SOCK_FILE ];then
    echo "-> Removing stale webservice socket"
    rm -f $SOCK_FILE
fi

echo "-> Executing $SCRIPT_PATH"
echo "-> LOG: $LOG_FILE"
echo "-> SOCKET: $SOCK_FILE"
echo "-> APP_CONFIG: $CONF_FILE"

echo "-> Starting gunicorn"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS
export PYTHONPATH=$APP_PROJECT_ROOT:$PYTHONPATH

cd $APP_PROJECT_ROOT \
&& . $APP_PROJECT_VENV/bin/activate \
&& gunicorn \
    $DJANGO_WSGI:application \
    --name {{ project_name }} \
    --user $APP_USER \
    --group $APP_USER \
    --workers $NUM_WORKERS \
    --threads $NUM_THREADS \
    --timeout $TIMEOUT \
    --bind=unix:$SOCK_FILE \
    --log-level=$LOG_LEVEL \
    --log-file=$LOG_FILE \
    --pid=$PID_FILE \
    --reload
