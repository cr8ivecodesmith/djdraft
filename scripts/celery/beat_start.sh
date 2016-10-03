#!/bin/bash

LOGS_DIR=$PROJECT_APP_DIR/var/logs
RUN_DIR=$PROJECT_APP_DIR/var/run
WORK_DIR=$PROJECT_APP_DIR/var/db

echo "-> Starting celery beat"
. $PROJECT_APP_VENV/bin/activate
cd $PROJECT_APP_DIR
python manage.py celery beat \
    --pidfile=$RUN_DIR/beat.pid \
    --logfile=$LOGS_DIR/beat.log \
    --workdir=$WORK_DIR \
    --loglevel=INFO \
    --detach
