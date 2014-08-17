Django DRAFT
============

The (D)jango (R)ESTFramework (A)pp(F)u (T)emplate

This is, ideally, a single app Django project template built with DRF and social
logins. Built as a hackathon starter boilerplate in mind.

Based on bleeding edge Django 1.7x

Uses Twitter as default social auth login


## Prerequisites


### External libs for Pillow

See: https://pillow.readthedocs.org/en/latest/installation.html#simple-installation

```
$ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
```


### Virtualenv

You should have a virtualenv ready with either Python 2.7.x or 3.x


### Database

This app is configured with PostgreSQL/MySQL in mind.


### Configuration

Under your project's settings folder you'll find a `config.json` file. Fill it out with the needed
values. Alternatively you can also create a `config-user.json` for configurations specific to a
particular environment.


### Server settings

TODO


## Usage

If you named your app `your_app_name`:

```
$ django-admin startproject --template=https://github.com/cr8ivecodesmith/djdraft/archive/master.zip --extension=py,html,json your_app_name
```
