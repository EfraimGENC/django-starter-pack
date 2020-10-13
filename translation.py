# Shell
## https://docs.djangoproject.com/en/3.1/ref/django-admin/#makemessages
django-admin.py makemessages --all #for all lang
django-admin.py makemessages -l en #for one lang only

## https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-compilemessages
django-admin compilemessages #Compiles .po files created by makemessages to .mo files for use with the built-in gettext support.
