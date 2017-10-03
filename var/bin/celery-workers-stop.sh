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
PID_FILE="$APP_PROJECT_ROOT/var/run/celery-workers.pid"
CELERY_PROJ=app
WORKERS="w1 w2"


cd $APP_PROJECT_ROOT \
&& . $APP_PROJECT_VENV/bin/activate \
&& celery multi stopwait $WORKERS \
    -A $CELERY_PROJ \
    -l INFO \
    --pidfile=$PID_FILE
