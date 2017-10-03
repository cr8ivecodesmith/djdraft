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
LOG_FILE="$APP_PROJECT_ROOT/var/log/celery-workers.log"
PID_FILE="$APP_PROJECT_ROOT/var/run/celery-workers.pid"
CELERY_PROJ=app
WORKERS="w1 w2"

# Restart workers if there is a pid file
if [ -f $PID_FILE ];then
    echo "-> Restarting celery workers"
    . $APP_PROJECT_ROOT/var/bin/celery-workers-restart.sh
    exit 0
fi

cd $APP_PROJECT_ROOT \
&& . $APP_PROJECT_VENV/bin/activate \
&& celery multi start $WORKERS \
    -A $CELERY_PROJ \
    -l INFO \
    --logfile=$LOG_FILE \
    --pidfile=$PID_FILE
