import os
import requests

MAIN_SERVICE_URL = str(os.getenv('MAIN_SERVICE_URL_DEV')) \
    if bool(os.getenv('AUX_DEBUG')) else str(os.getenv('MAIN_SERVICE_URL_PROD'))


def create_user(profile_id: str):
    is_deleted_sync = True
    try:
        response = requests.post(
            url=f'{MAIN_SERVICE_URL}/custom_auth/integration/create_user/',
            json={
                'profile_id': profile_id
            }
        )
        response.raise_for_status()
        message = response.text
    except (requests.exceptions.HTTPError,) as e:
        is_deleted_sync = False
        message = f"Error: {e}"

    return is_deleted_sync, message


def delete_user(profile_id: str):
    is_deleted_sync = True
    try:
        response = requests.delete(
            url=f'{MAIN_SERVICE_URL}/custom_auth/integration/delete_user/{profile_id}'
        )
        response.raise_for_status()
        message = response.text
    except (requests.exceptions.HTTPError,) as e:
        is_deleted_sync = False
        message = f"Error: {e}"

    return is_deleted_sync, message
