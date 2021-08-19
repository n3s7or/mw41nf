from mw42nf import request_json_rpc_sync, bind_self


@bind_self
def Connect(self) -> dict:
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='3.2'
    )


@bind_self
def DisConnect(self) -> dict:
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='3.3'
    )


@bind_self
def GetSystemStatus(self) -> dict:
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='13.4'
    )
