#!/bin/bash

if [[ $APP_ENV == dev* ]]; then
    echo "--> [dev] Building dev requirements"
    cd $PROJECT_APP_DIR \
        && make build_dev

    echo "--> [dev] Running migrations"
    su - $PROJECT_APP_USER -c """
    source $PROJECT_APP_VENV/bin/activate
    cd $PROJECT_APP_DIR
    python manage.py migrate
    """ > /dev/null

    echo "--> [dev] Starting celery"
    su - $PROJECT_APP_USER -c """
    source $PROJECT_APP_VENV/bin/activate
    cd $PROJECT_APP_DIR
    make beat_start && make workers_start
    """ > /dev/null

    echo "--> [dev] Starting web service"
    su - $PROJECT_APP_USER -c """
    source $PROJECT_APP_VENV/bin/activate
    cd $PROJECT_APP_DIR
    python manage.py runserver_plus 0.0.0.0:8000 --settings=app.settings.$APP_ENV &
    """ > /dev/null
elif [[ $APP_ENV == prod* ]]; then
    echo "--> [prod] Starting celery"
    su - $PROJECT_APP_USER -c """
    source $PROJECT_APP_VENV/bin/activate
    cd $PROJECT_APP_DIR
    make beat_start && make workers_start
    """ > /dev/null

    echo "--> [prod] Starting web service"
    cd $PROJECT_APP_DIR && make gunicorn_restart &

    echo "--> [prod] Starting ssh service"
    /usr/sbin/sshd -D
fi
