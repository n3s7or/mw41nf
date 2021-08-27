from mw42nf import request_json_rpc_sync, bind_self
from .models import Response


# START User's functions
@bind_self
def Login(self) -> dict:  # 1.1
    raise Exception('TODO')


@bind_self
def Logout(self) -> dict:  # 1.2
    raise Exception('TODO')


@bind_self
def GetLoginState(self) -> dict:  # 1.3
    raise Exception('TODO') \
 \
 \
@bind_self
def ChangePassword(self) -> dict:  # 1.4
    raise Exception('TODO')


@bind_self
def HeartBeat(self) -> dict:  # 1.5
    raise Exception('TODO')


@bind_self
def ForceLogin(self) -> dict:  # 1.6
    raise Exception('TODO')


@bind_self
def SetPasswordChangeFlag(self) -> dict:  # 1.7
    raise Exception('TODO')


@bind_self
def GetPasswordChangeFlag(self) -> dict:  # 1.8
    raise Exception('TODO')


@bind_self
def GetAutoRemenberPassword(self) -> dict:  # 1.9
    raise Exception('TODO')


@bind_self
def SetAutoRemenberPassword(self) -> dict:  # 1.10
    raise Exception('TODO')


# END User's functions
# ==================================
# START SIM functions


# END SIM functions
# ==================================
# START Connection functions


@bind_self
def GetConnectionState(self) -> Response:  # 3.1
    return Response(
        request_json_rpc_sync(
            self.__name__,
            params='',
            _id='3.1'
        ))


@bind_self
def Connect(self) -> dict:  # 3.2
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='3.2'
    )


@bind_self
def DisConnect(self) -> dict:  # 3.3
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='3.3'
    )


@bind_self
def GetConnectionSettings(self) -> Response:  # 3.4
    return Response(
        request_json_rpc_sync(
            self.__name__,
            params='',
            _id='3.4'
        ))


@bind_self
def SetConnectionSettings(self) -> dict:  # 3.5
    raise Exception('TODO')


# END Connection functions
# ==================================
# START Network functions


# TODO


# END Network functions
# ==================================
# START Wlan functions


# TODO


# END Wlan functions
# ==================================
# START SMS functions

@bind_self
def GetSMSInitStatus(self) -> dict:  # 6.1
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='6.1'
    )


@bind_self
def GetSMSContactList(self) -> dict:  # 6.2
    raise Exception('TODO')


@bind_self
def GetSMSContentList(self) -> dict:  # 6.3
    raise Exception('TODO')


@bind_self
def GetSMSStorageState(self) -> dict:  # 6.4
    raise Exception('TODO')


@bind_self
def DeleteSMS(self) -> dict:  # 6.5
    raise Exception('TODO')


@bind_self
def SendSMS(self) -> dict:  # 6.6
    raise Exception('TODO')


@bind_self
def GetSendSMSResult(self) -> dict:  # 6.7
    raise Exception('TODO')


@bind_self
def SaveSMS(self) -> dict:  # 6.8
    raise Exception('TODO')


@bind_self
def GetSMSSettings(self) -> dict:  # 6.9
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='6.9'
    )


@bind_self
def SetSMSSettings(self) -> dict:  # 6.10
    raise Exception('TODO')


@bind_self
def GetSingleSMS(self) -> dict:  # 6.11
    raise Exception('TODO')


# END SMS functions
# ==================================
# START Statistics functions


# TODO


# END Statistics functions
# ==================================
# START USSD functions

@bind_self
def SendUSSD(self) -> dict:  # 8.1
    raise Exception('TODO')


@bind_self
def GetUSSDSendResult(self) -> dict:  # 8.2
    raise Exception('TODO')


@bind_self
def SetUSSDEnd(self) -> dict:  # 8.3
    raise Exception('TODO')


# END USSD functions
# ==================================
# START  functions


# TODO


# END  functions
# ==================================
# START  functions


@bind_self
def GetSystemStatus(self) -> dict:
    return request_json_rpc_sync(
        self.__name__,
        params='',
        _id='13.4'
    )
