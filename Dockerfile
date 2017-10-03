FROM python:3.6

# Build env vars
ARG BUILD_ROOT /opt

# App env vars
ENV APP_ENV prod
ENV APP_USER caffeine
ENV APP_USER_HOME /home/caffeine
ENV APP_PROJECT_ROOT /home/caffeine/project
ENV APP_PROJECT_VENV /home/caffeine/venv

# Create non-priv user
RUN useradd \
    --user-group \
    --uid 1000 \
    --shell /bin/bash \
    --home-dir $APP_USER_HOME \
    $APP_USER

# Create virtualenv
RUN python -m venv $APP_PROJECT_VENV

# Install requirements
WORKDIR $BUILD_ROOT
COPY requirements/*.txt $BUILD_ROOT
RUN . $APP_PROJECT_VENV/bin/activate \
    && pip install \
        --no-cache-dir --no-compile \
        --log $BUILD_ROOT/pip.log \
        -U pip \
    && pip install \
        --no-cache-dir --no-compile \
        --log $BUILD_ROOT/pip.log \
        -r $APP_ENV.txt

# Fix permissions
RUN chown $APP_USER: -R $APP_USER_HOME

# Clean up
RUN apt-get autoclean \
    && apt-get autoremove --purge \
    && rm -rf $BUILD_ROOT/*

# Start
WORKDIR $APP_PROJECT_ROOT
