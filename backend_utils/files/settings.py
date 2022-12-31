from django.conf import global_settings, settings

DEBUG = getattr(settings, 'DEBUG')

STATIC_URL = getattr(settings, 'STATIC_URL')

MEDIA_URL = getattr(settings, 'MEDIA_URL')

FILE_STORAGES = getattr(settings, 'FILE_STORAGES')

DEFAULT_FILE_STORAGE = global_settings.DEFAULT_FILE_STORAGE

STATICFILES_STORAGE = global_settings.STATICFILES_STORAGE
