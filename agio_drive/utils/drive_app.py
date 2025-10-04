import requests


def is_active():
    try:
        requests.get('http://localhost:9085/swagger/index.html', timeout=1)
        return True
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as e:
        print(f'{e.__class__.__module__}.{e.__class__.__name__}:', e)
        return False
