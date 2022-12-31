from typing import Dict

from storages.backends.s3boto3 import S3Boto3Storage

from .settings import MEDIA_URL, STATIC_URL
from .utils import parse_storage_url


class AWSS3Storage(S3Boto3Storage):
    storage_name = ''
    init_params: Dict[str, str] = {}

    def __init__(self, *args, **kwargs):
        main_params = {**self.init_params, **kwargs}
        url_params = {}

        if STATIC_URL and self.storage_name == 'static':
            url_params = parse_storage_url(STATIC_URL)

        if MEDIA_URL and self.storage_name == 'media':
            url_params = parse_storage_url(MEDIA_URL)

        storage_url = main_params.pop('url', '')

        if not isinstance(storage_url, str):
            raise ValueError

        if storage_url:
            url_params = parse_storage_url(storage_url)

        super().__init__(*args, **url_params, **main_params)
