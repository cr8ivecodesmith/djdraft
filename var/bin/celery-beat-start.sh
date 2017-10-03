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
LOG_FILE="$APP_PROJECT_ROOT/var/log/celery-beat.log"
PID_FILE="$APP_PROJECT_ROOT/var/run/celery-beat.pid"
CELERY_PROJ=app

# Delete any existing pid files
if [ -f $PID_FILE ];then
    echo "-> Stopping celery beat"
    (cat $PID_FILE | xargs kill -15) || echo "" && rm -f $PID_FILE
fi

echo "-> Starting celery beat"
cd $APP_PROJECT_ROOT \
&& . $APP_PROJECT_VENV/bin/activate \
&& celery beat \
    -A $CELERY_PROJ \
    -S django \
    -l INFO \
    --logfile=$LOG_FILE \
    --pidfile=$PID_FILE \
    --detach
