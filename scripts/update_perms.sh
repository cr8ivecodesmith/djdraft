#!/bin/bash

# Make sure that the docker container can write to these directories
echo "-> Updating permissions and ownership for docker access"

find $PROJECT_APP_DIR -iname "migrations" -type "d" | xargs chmod 777
find $PROJECT_APP_VENV -iname "migrations" -type "d" | xargs chmod 777

chmod 777 $PROJECT_APP_DIR/db
chmod 777 $PROJECT_APP_DIR/run
chmod 777 $PROJECT_APP_DIR/logs
chmod 777 $PROJECT_APP_DIR/logs/*.log
chmod 777 $PROJECT_APP_DIR/static

find $PROJECT_APP_DIR/static -iname "*.js" | xargs chmod 755
find $PROJECT_APP_DIR/static -iname "*.css" | xargs chmod 755

chown -R $PROJECT_APP_USER: $PROJECT_APP_VENV
