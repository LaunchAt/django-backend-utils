import boto3
from watchtower import CloudWatchLogHandler


class AmazonCloudWatchLoggingHandler(CloudWatchLogHandler):
    def __init__(self, *args, **kwargs):
        log_group_name = kwargs.pop('log_group_name', '')
        access_key = kwargs.pop('access_key', '')
        secret_key = kwargs.pop('secret_key', '')
        region_name = kwargs.pop('region_name', '')
        kwargs.update(
            {
                'boto3_client': boto3.client(
                    'logs',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    region_name=region_name,
                ),
            }
        )

        if log_group_name:
            kwargs.update({'log_group_name': log_group_name})

        try:
            super().__init__(*args, **kwargs)

        except Exception:
            pass
