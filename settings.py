MIDDLEWARE = [
'django.middleware.locale.LocaleMiddleware', #after sessions.middleware
]

USE_I18N = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('tr', _('Turkish')),
    ('en', _('English')),
)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')