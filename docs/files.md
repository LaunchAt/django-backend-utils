# Storage Utilities

## Storage Class

There are two base storage classes to set up custom storage:

* `StaticStorage`
* `MediaStorage`

These are set up dynamically on load by settings on `settings.FILE_STORAGES`.

And you can also create dynamically your own storage as you need with `get_custom_storage_class`.

Example:

```python
from backend_utils.files.storage import get_custom_storage_class

CustomExapmleStorage = get_custom_storage_class('custom_example')
```

The `StaticStorage` and the `MediaStorage` are made by `get_custom_storage_class` as same.

If no storage is set in `settings.FILE_STORAGES` or default on debugging (`DEBUG = True`), they use Django's default storages.

### `StaticStorage`

The dynamic storage class for static files.

Setting `settings.STATICFILES_STORAGE` as `backend_utils.files.storage.StaticStorage` to use this storage.

If the setting is the default, it uses `django.contrib.staticfiles.storage.StaticFilesStorage` when debugging,

### `MediaStorage`

The dynamic storage class for media files.

Setting `settings.DEFAULT_FILE_STORAGE` as `backend_utils.files.storage.MediaStorage` to use this storage.

If the setting is the default, it uses `django.core.files.storage.FileSystemStorage` when debugging,

## `AWSS3Storage`

The storage is set up to use the AWS S3 bucket (and CloudFront as you need).

It should be set as a `class` in `settings.FILE_STORAGES.<storage_name>`.

Attributes:

* `access_key`: The Access Key ID of the IAM User with required permissions for the target S3 bucket.
* `secret_key`: The Secret Access Key of the IAM User set up with `access_key`.
* `bucket_name`: The AWS S3 bucket name.
* `region_name`: The AWS S3 region name.
* `url`: The AWS S3 access URL or the CloudFront resource URL. It should have the HTTPS protocol, a valid hostname, and a valid path longer than `/`. If you use CloudFront, the URL should be of CloudFront.

You can use the following attributes as alternatives to `url`.

* `custom_domain`: The custom domain in the AWS S3 access URL or the CloudFront resource URL.
* `location`: The location path in the AWS S3 access URL or the CloudFront resource URL.

If you use the `StaticStorage` as `settings.STATICFILES_STORAGE`,
uses `settings.STATIC_URL` as the default `url`.

And Of course, if you use the `MediaStorage` as `settings.DEFAULT_FILE_STORAGE`,
uses `settings.MEDIA_URL` as the default `url`.

## Settings

You can use these utils, using the following settings.

* `settings.STATIC_ROOT`: See more on Django's official documentation.
* `settings.STATIC_URL`: See more on Django's official documentation.
* `settings.MEDIA_ROOT`: See more on Django's official documentation.
* `settings.MEDIA_URL`: See more on Django's official documentation.
* `settings.DEFAULT_FILE_STORAGE`: See more on Django's official documentation.
* `settings.STATICFILES_STORAGE`: See more on Django's official documentation.
* `settings.FILE_STORAGES`: It should be set keys and values for some file storages.

The storage settings in `settings.FILE_STORAGES` are read in the certain rules:

* The `CustomExapmpleStorage` read `settings.FILE_STORAGES.default` and `settings.FILE_STORAGES.custom_example` in turn.
* Later read values will overwrite the `settings.FILE_STORAGES.default` values.
* If `settings.DEBUG` is `True`, read `settings.FILE_STORAGES.default.debug` and `settings.FILE_STORAGES.custom_example.debug` in turn.

The `settings.FILE_STORAGES` type is described following.

```python
FILE_STORAGES = {
    # The `settings.FILE_STORAGES.default` is the common setting enabled
    # on all storages.
    # Specify the class dotted path and attributes to give the class.
    'default': {
        'class': str,
        '<CLASS_ATTRIBUTE_NAME_1>': str,
        '<CLASS_ATTRIBUTE_NAME_2>': str,
        '<CLASS_ATTRIBUTE_NAME_3>': str,
        ...,
        # If you want to use custom storage in debugging,
        # you should set `debug` as `True` or a dictionary that
        # overrides default settings.
        # If the `debug` value is estimated as `False`,
        # Django's default storage is selected.
        'debug': bool,
        'debug': {
            'class': ,
            '<CLASS_ATTRIBUTE_NAME_1>': str,
            '<CLASS_ATTRIBUTE_NAME_2>': str,
            '<CLASS_ATTRIBUTE_NAME_3>': str,
            ...,
        },
    },
    # If you want to use custom storage overriding the default settings,
    # you should set a dictionary that has your custom storage name in
    # the snake case as the key, and has a dictionary as the value that
    # overrides default settings.
    'custom_exapmle': {  # Example for `CustomExampleStorage` class
        'class': str,
        '<CLASS_ATTRIBUTE_NAME_1>': str,
        '<CLASS_ATTRIBUTE_NAME_2>': str,
        '<CLASS_ATTRIBUTE_NAME_3>': str,
        ...,
        # If you want to use custom storage in debugging, you should
        # have a dictionary that overrides default `debug` settings.
        'debug': bool,
        'debug': {
            'class': ,
            '<CLASS_ATTRIBUTE_NAME_1>': str,
            '<CLASS_ATTRIBUTE_NAME_2>': str,
            '<CLASS_ATTRIBUTE_NAME_3>': str,
            ...,
        },
    },
}
```

### Exapmle

```python
# settings.py

import os

# Static and media files

STATIC_ROOT = 'static/'

STATIC_URL = os.getenv('DJANGO_STATIC_URL')

MEDIA_ROOT = 'media/'

MEDIA_URL = os.getenv('DJANGO_MEDIA_URL')

DEFAULT_FILE_STORAGE = 'backend_utils.files.storage.MediaStorage'

STATICFILES_STORAGE = 'backend_utils.files.storage.StaticStorage'

FILE_STORAGES = {
    'default': {
        'class': 'backend_utils.files.aws_s3.AWSS3Storage',
        'access_key': os.getenv('AWS_ACCESS_KEY_ID'),
        'secret_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
        'bucket_name': os.getenv('AWS_S3_BUCKET_NAME'),
        'region_name': os.getenv('AWS_REGION_NAME'),
    },
}
```
