# Logging Utilities

## Logging Handler Class

### `AmazonCloudWatchLoggingHandler`

A logging handler connect and report to your log group in the AWS Cloudwatch Logging.

You can use this utils by setting the configuration in `settings.LOGGING.handlers`.

```python
# settings.py

# Logging

LOGGING = {
    ...
    'handlers': {
        ...
        'cloudwatch': {
            ...
            'class': 'backend_utils.logging.handlers.AmazonCloudWatchLoggingHandler',
            'log_group_name': str,
            'access_key': str,
            'secret_key': str,
            'region_name': str,
        },
    },
}
```

Example:

Set the level as `DEBUG` and you should do level controlling in loggers.

And add `require_debug_false` to the filters, only available in `DEBUG = False`.

```python
# settings.py

ipmort os

# Logging

LOGGING = {
    ...
    'handlers': {
        ...
        'cloudwatch': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'backend_utils.logging.handlers.AmazonCloudWatchLoggingHandler',
            'formatter': 'default',
            'log_group_name': os.getenv('AWS_CLOUDWATCH_LOG_GROUP_NAME'),
            'access_key': os.getenv('AWS_ACCESS_KEY_ID'),
            'secret_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
            'region_name': os.getenv('AWS_REGION_NAME'),
        },
    },
}
```
