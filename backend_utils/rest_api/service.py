import logging

import boto3
from rest_framework.exceptions import NotFound, Throttled

from .settings import (
    AWS_COGNITO_ACCESS_KEY_ID,
    AWS_COGNITO_REGION_NAME,
    AWS_COGNITO_SECRET_ACCESS_KEY,
    AWS_COGNITO_USER_POOL_ID,
)

logger = logging.getLogger(__name__)


class CognitoService:
    client = boto3.client(
        'cognito-idp',
        aws_access_key_id=AWS_COGNITO_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_COGNITO_SECRET_ACCESS_KEY,
        region_name=AWS_COGNITO_REGION_NAME,
    )

    def delete_cognito_user(self: 'CognitoService', user_id: str) -> None:
        try:
            self.client.admin_delete_user(
                UserPoolId=AWS_COGNITO_USER_POOL_ID,
                Username=user_id,
            )

        except self.client.exceptions.TooManyRequestsException as error:
            logger.error(f'{type(error)}: {error}')
            raise Throttled(wait=5) from error

        except self.client.exceptions.UserNotFoundException as error:
            logger.error(f'{type(error)}: {error}')
            raise NotFound from error
