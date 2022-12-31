import re

from .settings import FILE_STORAGES
from .utils import get_custom_storages

custom_storages = get_custom_storages(FILE_STORAGES)

storage_name_pattern = re.compile(r'^[a-z][a-z0-9_]+[a-z0-9]$')


def get_custom_storage_class(storage_name):
    result = storage_name_pattern.match(storage_name)

    if not result or result.group() != storage_name:
        raise ValueError

    custom_storage = custom_storages.get(storage_name)

    assert custom_storage

    storage_class = custom_storage.get('class')
    storage_params = custom_storage.get('params')
    class_name_prefix = ''.join(map(str.capitalize, storage_name.split('_')))

    return type(
        f'{class_name_prefix}Storage',
        (storage_class,),
        {'storage_name': storage_name, 'init_params': storage_params},
    )


StaticStorage = get_custom_storage_class('static')

MediaStorage = get_custom_storage_class('media')
