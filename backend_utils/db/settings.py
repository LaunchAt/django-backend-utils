from django.conf import settings

DATABASES = getattr(settings, 'DATABASES')
