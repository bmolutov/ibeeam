import os
import requests


MAIN_SERVICE_URL = str(os.getenv('MAIN_SERVICE_URL_DEV')) \
    if bool(os.getenv('DEBUG')) else str(os.getenv('MAIN_SERVICE_URL_PROD'))


def create_user(profile_id: str):
    response = requests.post(
        url=f'{MAIN_SERVICE_URL}/custom_auth/integration/create_user/',
        json={
            'profile_id': profile_id
        }
    )
    return response.text


def delete_user(profile_id: str):
    response = requests.delete(
        url=f'{MAIN_SERVICE_URL}/custom_auth/integration/delete_user/{profile_id}'
    )
    return response.text
