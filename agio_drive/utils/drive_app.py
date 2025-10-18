import requests

BASE_URL = 'http://localhost:9085'


def is_active():
    try:
        requests.get(f'{BASE_URL}/swagger/index.html', timeout=1)
        return True
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as e:
        print(f'{e.__class__.__module__}.{e.__class__.__name__}:', e)
        return False


def get_mount_paths():
    if not is_active():
        return
    return requests.get(f'{BASE_URL}/mount', timeout=1).json()
