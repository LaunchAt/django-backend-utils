from django.conf import settings

AUTH_USER_MODEL = getattr(
    settings,
    'AWS_COGNITO_AUTH_USER_MODEL',
    settings.AUTH_USER_MODEL,
)

AWS_COGNITO_ACCESS_KEY_ID = getattr(settings, 'AWS_COGNITO_ACCESS_KEY_ID', '')

AWS_COGNITO_CLIENT_ID = getattr(settings, 'AWS_COGNITO_CLIENT_ID', '')

AWS_COGNITO_JWKS = getattr(settings, 'AWS_COGNITO_JWKS', {})

AWS_COGNITO_REGION_NAME = getattr(settings, 'AWS_COGNITO_REGION_NAME', '')

AWS_COGNITO_SECRET_ACCESS_KEY = getattr(settings, 'AWS_COGNITO_SECRET_ACCESS_KEY', '')

AWS_COGNITO_USER_POOL_ID = getattr(settings, 'AWS_COGNITO_USER_POOL_ID', '')

AWS_COGNITO_ENDPOINT = 'https://cognito-idp.{}.amazonaws.com/{}'.format(
    AWS_COGNITO_REGION_NAME,
    AWS_COGNITO_USER_POOL_ID,
)
