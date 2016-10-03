FROM ubuntu:14.04

# Build time env vars
ARG BUILD_DIR=/_build/
ARG BASE_REQ=/_build/requirements/build.sh
ARG BASE_PIP=/_build/requirements/base.txt

# Project env vars
# NOTE:
# - Change APP_ENV to `prod` when building for production
# - A non-priv user named `caffeine` will be created with home dir at `/srv/caffeine`
# - A sudoer user named `happy` will be created for ssh login
# - a virtualenv called `venv` will be created
ENV APP_ENV=dev
ENV VENV_NAME=venv
ENV PROJECT_APP_USER=caffeine
ENV PROJECT_APP_HOME=/srv/caffeine
ENV PROJECT_APP_DIR=/srv/caffeine/project
ENV PROJECT_APP_VENV=/srv/caffeine/venv
ENV PROJECT_SUDO_USER=happy
ENV PROJECT_SUDO_PASS=happy@1234

RUN mkdir -p $BUILD_DIR
WORKDIR $BUILD_DIR
ADD . $BUILD_DIR

# Install packages and build the environment
RUN apt-get update && apt-get install -y \
       build-essential \
       python3-dev \
       python3-pip \
       python3.4-venv \
       openssh-server \
       htop \
    && . $BASE_REQ \
    && pip3 install -U pip \
    && mkdir /var/run/sshd \
    && make init_env

# Clean up
RUN apt-get autoclean \
    && apt-get autoremove \
    && apt-get purge \
    && rm -Rf $BUILD_DIR

EXPOSE 22 8000

CMD ["/usr/sbin/sshd", "-D"]
