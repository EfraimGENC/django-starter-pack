# Django Starter Pack
It's for fast start to new django project.

> Project Name: `mysite`
> Virtual Enviorment Name: `myvenv`
> App Name: `myapp`

## Let's Start
`$ mkdir mysite`

`$ cd mysite`

`$ python3 -m venv myvenv`

`$ source myvenv/bin/activate`

`$ python3 -m pip install --upgrade pip`

`$ django-admin startproject mysite .`

`$ python3 manage.py startapp myapp`

`$ python3 manage.py migrate`

`add app to INSTALLED_APPS in setttings.py`

`$ python3 manage.py makemigrations`

`$ python3 manage.py migrate`

`$ python manage.py createsuperuser`