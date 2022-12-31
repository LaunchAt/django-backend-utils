import copy
import re
from urllib.parse import urlparse

from django.utils.module_loading import import_string

from .settings import DEBUG, DEFAULT_FILE_STORAGE, STATICFILES_STORAGE


def get_storage_class(class_name='', storage_name=''):
    default_storage_class_name = DEFAULT_FILE_STORAGE

    if storage_name == 'static':
        default_storage_class_name = STATICFILES_STORAGE

    return import_string(class_name or default_storage_class_name)


def parse_storage_config(config={}):
    storage_params = copy.deepcopy(config)
    storage_class_name = storage_params.pop('class', '')

    if not isinstance(storage_class_name, str):
        raise ValueError

    if DEBUG:
        debug_config = storage_params.pop('debug', None)

        if debug_config:
            if not isinstance(debug_config, (dict, bool)):
                raise ValueError
        else:
            return '', {}

        if isinstance(debug_config, dict):
            debug_storage_class_name = debug_config.pop('class', '')

            if not isinstance(debug_storage_class_name, str):
                raise ValueError

            storage_class_name = debug_storage_class_name or storage_class_name
            storage_params.update(debug_config)

    return storage_class_name, storage_params


def get_custom_storages(config):
    if not isinstance(config, dict):
        raise ValueError

    storages_config = copy.deepcopy(config)
    default_config = storages_config.pop('default', {})

    if not isinstance(default_config, dict):
        raise ValueError

    default_class_name, default_params = parse_storage_config(default_config)

    custom_storages = {}
    storage_names = list(set(['static', 'media', *storages_config.keys()]))

    for storage_name in storage_names:
        custom_config = storages_config.get(storage_name, {})

        if not isinstance(custom_config, dict):
            raise ValueError

        custom_class_name, custom_params = parse_storage_config(custom_config)

        custom_storages[storage_name] = {
            'class': get_storage_class(
                class_name=default_class_name or custom_class_name,
                storage_name=storage_name,
            ),
            'params': {**default_params, **custom_params},
        }

    return custom_storages


def parse_storage_url(url):
    parsed_url = urlparse(url)

    if parsed_url.scheme != 'https':
        raise ValueError

    if not parsed_url.hostname or not parsed_url.path:
        raise ValueError

    return {
        'custom_domain': parsed_url.hostname,
        'location': re.sub('^/', '', parsed_url.path),
    }
