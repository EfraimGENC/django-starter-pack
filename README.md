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

$ django-admin startproject mysite .

$ python3 manage.py startapp myapp

$ python3 manage.py migrate
```
add app to INSTALLED_APPS in setttings.py
```bash
$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python manage.py createsuperuser
```

> Multi Language Shell Commands:
https://docs.djangoproject.com/en/3.1/ref/django-admin/#makemessages
`django-admin.py makemessages --all` #for all lang
`django-admin.py makemessages -l en` #for one lang only

https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-compilemessages
`django-admin compilemessages` #Compiles .po files created by makemessages to .mo files for use with the built-in gettext support.