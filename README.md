# Django Starter Pack
It's for fast start to new django project.

## Let's Start

> Project Name: **mysite**
Virtual Enviorment Name: **myvenv**
App Name: **myapp**

```bash
$ mkdir mysite

$ cd mysite

$ python3 -m venv myvenv

$ source myvenv/bin/activate

$ python3 -m pip install --upgrade pip

$ pip3 install django

$ django-admin --version # to check

$ django-admin startproject mysite .

$ python3 manage.py migrate

$ python3 manage.py startapp myapp
```
**add app to INSTALLED_APPS in setttings.py**
```bash
$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py createsuperuser

$ deactivate # To leave your virtual environment
```

### Multi Language Shell Commands:
```bash
# to create .po files
django-admin.py makemessages --all  # for all lang
django-admin.py makemessages -l en  # for one lang onl
# to create .mo files from .po files
django-admin compilemessages  # Compiles .po files created by makemessages to .mo files for use with the built-in gettext support.
```