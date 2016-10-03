#!/bin/bash

PIP_BUILD=$1

su - $PROJECT_APP_USER -c """
source $PROJECT_APP_VENV/bin/activate
cd $PROJECT_APP_DIR
pip install -r requirements/${PIP_BUILD}.txt
deactivate
"""
