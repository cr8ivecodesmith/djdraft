Django DRAFT
============

The (D)jango (R)ESTFramework (A)pp(F)u (T)emplate

This is, ideally, a single app Django project template built with DRF and social
logins. Built as a hackathon starter boilerplate in mind.

Based on bleeding edge Django 1.7x

Uses Twitter as default social auth login


## Prerequisites

### Virtualenv

You should have a virtualenv ready with either Python 2.7.x or 3.x

### Database

This app is configured with PostgresSQL in mind.


### Environmental variables

This app uses your OS's environmental variables for certain settings values.
See: http://www.cyberciti.biz/faq/set-environment-variable-linux/

i.e.

If you named your app `your_app_name`, then you should create the ff. env vars:

```
YOUR_APP_NAME_DB_ENGINE
YOUR_APP_NAME_DB_NAME
YOUR_APP_NAME_DB_USER
YOUR_APP_NAME_DB_PASSWORD
YOUR_APP_NAME_DB_HOST
YOUR_APP_NAME_DB_PORT

YOUR_APP_NAME_SOCIAL_AUTH_TWITTER_KEY
YOUR_APP_NAME_SOCIAL_AUTH_TWITTER_SECRET
```

Troubleshooting notes:

If for some reason, you're app is having trouble finding the right env var, just directly initalize
the concerned variables in your settings file. Just don't commit your settings file ;)


## Usage

```
$ django-admin startproject --template=https://github.com/cr8ivecodesmith/djdraft/archive/master.zip --extension=py,rst,html your_app_name
```
