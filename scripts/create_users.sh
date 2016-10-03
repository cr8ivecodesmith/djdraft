#!/bin/bash

echo "--> Setting os environment variables"
echo "PROJECT_APP_USER=$PROJECT_APP_USER" >> /etc/environment
echo "PROJECT_APP_HOME=$PROJECT_APP_HOME" >> /etc/environment
echo "PROJECT_APP_DIR=$PROJECT_APP_DIR" >> /etc/environment
echo "PROJECT_APP_VENV=$PROJECT_APP_VENV" >> /etc/environment
echo "VENV_NAME=$VENV_NAME" >> /etc/environment
echo "APP_ENV=$APP_ENV" >> /etc/environment

echo "--> Refreshing os environment variables"
source /etc/environment

echo "--> Creating superuser '$PROJECT_SUDO_USER'"
useradd --user-group \
    --shell /bin/bash \
    --home-dir $PROJECT_APP_HOME \
    $PROJECT_SUDO_USER
echo $PROJECT_SUDO_USER:$PROJECT_SUDO_PASS | chpasswd
adduser $PROJECT_SUDO_USER sudo

echo "--> Creating application user '$PROJECT_APP_USER'"
mkdir -p $PROJECT_APP_HOME
useradd --system --user-group \
    --shell /bin/bash \
    --home-dir $PROJECT_APP_HOME \
    $PROJECT_APP_USER
chown $PROJECT_APP_USER: $PROJECT_APP_HOME

echo "--> Updating user '$PROJECT_SUDO_USER' and '$PROJECT_APP_USER' groups"
usermod -aG $PROJECT_APP_USER $PROJECT_SUDO_USER
usermod -aG $PROJECT_SUDO_USER $PROJECT_APP_USER
