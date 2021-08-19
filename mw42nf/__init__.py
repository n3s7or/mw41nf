import services


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
