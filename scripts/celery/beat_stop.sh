#!/bin/bash

RUN_DIR=$PROJECT_APP_DIR/var/run

echo "-> Stopping celery beat"
cat $RUN_DIR/beat.pid | xargs kill -9
