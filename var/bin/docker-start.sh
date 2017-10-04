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

# TODO:
# - install requirements
# - run migrations
# - update static files
# - start celery beat
# - start celery workers
# - start gunicorn
