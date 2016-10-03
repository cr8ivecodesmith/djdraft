#!/bin/bash

echo "-> Creating virtualenv and installing base requirements"
su - $PROJECT_APP_USER -c """
cd $PROJECT_APP_HOME
python3 -m venv $VENV_NAME
source $PROJECT_APP_VENV/bin/activate
pip install -r $BASE_PIP
deactivate
"""
