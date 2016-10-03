SHELL := /bin/bash

.PHONY:
	clean
	init_env
	build_base
	build_dev
	deploy
	create_app
	beat_start
	beat_stop
	beat_restart
	workers_start
	workers_stop
	workers_restart
	gunicorn_start
	gunicorn_stop
	gunicorn_restart

help:
	@echo "init_env - Initializes the base requirements and environment"
	@echo "build_[base|dev|prod] - Installs environmental requirements"
	@echo "beat_[start|stop|restart] - Manage celery beat"
	@echo "workers_[start|stop|restart] - Manage celery workers"
	@echo "gunicorn_[start|stop|restart] - Manage gunicorn"
	@echo "deploy - Deploys the specified environment"
	@echo "create_app - Creates app relative to the app dir"
	@echo "clean - remove all artifacts"

clean:
	find . -iname "*.pyc" | xargs rm -Rf
	find . -iname "*.pyo" | xargs rm -Rf
	find . -iname "*.pyd" | xargs rm -Rf
	find . -iname "__pycache__" | xargs rm -Rf

init_env:
	make clean
	source requirements/build.sh
	source scripts/create_users.sh
	source scripts/create_env.sh

build_base:
	make clean
	source requirements/build.sh
	source requirements/install_pip.sh base

build_dev:
	make build_base
	source scripts/update_perms.sh
	source requirements/install_pip.sh dev

build_prod:
	make build_base
	source scripts/update_perms.sh
	source requirements/install_pip.sh prod

deploy:
	source scripts/run_deploy.sh

beat_start:
	source scripts/celery/beat_start.sh

beat_stop:
	source scripts/celery/beat_stop.sh

beat_restart:
	(make beat_stop && make beat_start) || make beat_start

workers_start:
	source scripts/celery/$(APP_ENV)/start.sh

workers_stop:
	source scripts/celery/$(APP_ENV)/stop.sh

workers_restart:
	source scripts/celery/$(APP_ENV)/restart.sh

gunicorn_start:
	source scripts/gunicorn/stop.sh || echo "-> Nothing to stop"
	source scripts/gunicorn/start.sh

gunicorn_stop:
	source scripts/gunicorn/stop.sh

gunicorn_restart:
	(make gunicorn_stop && make gunicorn_start) || make gunicorn_start

create_app:
	source scripts/create_app.sh $(APP_NAME) $(APP_DIR)
