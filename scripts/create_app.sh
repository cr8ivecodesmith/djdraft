#!/bin/bash

APP_NAME=$1
APP_DIR=$2

echo "-> Creating django app"
source $PROJECT_APP_VENV/bin/activate
cd $PROJECT_APP_DIR/$APP_DIR
django-admin startapp $APP_NAME
deactivate
echo "-> done"
