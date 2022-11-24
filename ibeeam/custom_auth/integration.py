import requests
import environ


env = environ.Env()
environ.Env.read_env()


AUXILIARY_SERVICE_URL = str(env('AUXILIARY_SERVICE_URL_DEV')) \
    if bool(env('WEB_DEBUG')) else str(env('AUXILIARY_SERVICE_URL_PROD'))


def list_user_profiles():
    response = requests.get(
        url=f'{AUXILIARY_SERVICE_URL}/list_user_profiles'
    )
    return response.text


def get_user_profile(profile_id: str):
    response = requests.get(
        url=f'{AUXILIARY_SERVICE_URL}/get_user_profile/{profile_id}'
    )
    return response.text


def create_user_profile(user_profile_data: dict):
    response = requests.post(
        url=f'{AUXILIARY_SERVICE_URL}/create_user_profile',
        json=user_profile_data
    )
    return response.text


def update_user_profile(profile_id: str, user_profile_data):
    response = requests.put(
        url=f'{AUXILIARY_SERVICE_URL}/update_user_profile/{profile_id}',
        json=user_profile_data
    )
    return response.text


def delete_user_profile(profile_id: str):
    response = requests.delete(
        url=f'{AUXILIARY_SERVICE_URL}/delete_user_profile/{profile_id}'
    )
    return response.text


def get_favorite_posts_ids(profile_id: str):
    response = requests.get(
        url=f'{AUXILIARY_SERVICE_URL}/integration/users/{profile_id}/favorite_posts_ids'
    )
    return response.json()
