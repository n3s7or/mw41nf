import services
from enum import Enum


class ApiResult(Enum):
    SUCCESS = 0
    FAIL = 1


class NwType(Enum):
    GSM = 1
    UMTS = 2
    LTE = 3
    SCDMA = 9


def bind_self(func):
    # https://stackoverflow.com/a/5063783/7771926
    return func.__get__(func, type(func))


def request_json_rpc_sync(method, params, _id) -> dict:
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": _id
    }
    url = "/jrd/webapi?api=" + method

    return services.post(url=url, data=data)


def request_json_rpc_is_ok(result: dict) -> bool:
    if not result:
        return False

    keys = result.keys()
    return 'result' in keys and 'error' not in keys
