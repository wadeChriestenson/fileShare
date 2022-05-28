# **Baseline_** 
### Web App 

## Installation
Use the package manage [pip](https://pip.pypa.io/en/stable/) to install requirements.txt file 
to install all required packages.
```bash
pip install -r requirements.txt
```

## ***Baseline_*** - Backend Directory
- __init__.py
- asgi.py - (used for server setting)
- setting.py - (used for the full app settings, security, middleware, static directories, etc..)
- url.py - (used for routing back-end urls) - only has admin panrl and front-end urls
- wsgi.py - (used for more server settings)

## ***dashboard*** - Front-End Directory
- __init__.py
- admin.py - (set admin settings for django admin panel)- not in use
- apps.py - (unsure of use) - not in use
- migration - (changes made in the database) -not in use
- models.py - (used for creating database tables and pushes them into the migration directory)
- static - (directory used for holding Images, CSS files, Javascript files and CSV files)
- templates - (used for holding all html files)
- test.py - (used for writing test for the front-end)
- urls.py - (used for routing all urls in the front end)
- views.py - (used for writing the data that post to the html files) 

## ***.gitignore*** - used for ignore files in git.

## ***manage.py*** - used to run django app
To setup database use the following two commands.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
Use command below to run server on local host to view site in action.
```bash
python manage.py runserver
```
## ***db.sqlite*** - preinstalled once you run the django server
Database for user, admin and baseline data.


