#!/bin/bash

PIDFILE=$PROJECT_APP_DIR/var/run/gunicorn.pid

echo "-> Stopping gunicorn"
cat $PIDFILE | xargs kill -9
