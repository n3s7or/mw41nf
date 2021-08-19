import requests
import json
from json.decoder import JSONDecodeError
import settings


def _call(method, url, **kwargs) -> dict:
    r = requests.request(method, url, **kwargs)
    try:
        return r.json()
    except JSONDecodeError as e:
        return {
            'status': 'ko',
            'error': 'Wrong API JSON response'
        }


def get(url) -> dict:
    return _call('get', url)


def post(url: str, data: dict) -> dict:
    _url = settings.BACKEND_API + url
    return _call('post', _url, data=json.dumps(data))
