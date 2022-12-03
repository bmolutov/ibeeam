import os
import requests

MAIN_SERVICE_URL = str(os.getenv('MAIN_SERVICE_URL_DEV')) \
    if bool(os.getenv('AUX_DEBUG')) else str(os.getenv('MAIN_SERVICE_URL_PROD'))


def create_user(username: str, password: str):
    is_deleted_sync = True
    try:
        response = requests.post(
            url=f'{MAIN_SERVICE_URL}/integration/create_user/',
            json={
                'username': username,
                'password': password
            }
        )
        response.raise_for_status()
        message = response.text
    except (requests.exceptions.HTTPError,) as e:
        is_deleted_sync = False
        message = f"Error: {e}"

    return is_deleted_sync, message


def delete_user(username: str):
    is_deleted_sync = True
    try:
        response = requests.delete(
            url=f'{MAIN_SERVICE_URL}/integration/delete_user/{username}'
        )
        response.raise_for_status()
        message = response.text
    except (requests.exceptions.HTTPError,) as e:
        is_deleted_sync = False
        message = f"Error: {e}"

    return is_deleted_sync, message
