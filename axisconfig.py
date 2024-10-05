import requests
from requests.auth import HTTPDigestAuth

class Request:
    def __init__(self, host: str, port, username: str, password: str) -> None:
        self.timeout:int = 10
        self.base_url:str = f'http://{host}:{port}/'
        self.__username:str = username
        self.__password:str = password

    def __repr__(self):
        return f"<AxisCgi: {self.base_url}>"

    def api_discovery(self, params=None, json=None) -> requests.Response:
        return requests.post(self.base_url + 'axis-cgi/apidiscovery.cgi', params=params, json=json, auth=HTTPDigestAuth(self.__username, self.__password))
    
    def audio_device_control(self, params=None) -> requests.Response:
        return requests.post(self.base_url + 'axis-cgi/audiodevicecontrol.cgi', params=params, auth=HTTPDigestAuth(self.__username, self.__password))

    def audio_transmit(self, params=None, body=None) -> requests.Response:
        return requests.post(self.base_url + 'axis-cgi/audio/transmit.cgi', params=params, json=body,  auth=HTTPDigestAuth(self.__username, self.__password))

    def audio_recive(self, params=None) -> requests.Response:
        return requests.get(self.base_url + f'axis-cgi/audio/receive.cgi', params=params, auth=HTTPDigestAuth(self.__username, self.__password))

    def basic_device_info(self, params=None, json=None) -> requests.Response:
        return requests.post(self.base_url + 'axis-cgi/basicdeviceinfo.cgi', params=params, json=json,auth=HTTPDigestAuth(self.__username, self.__password))
        
    def capture_mode(self, params=None) -> requests.Response:
        return requests.post(self.base_url + f'axis-cgi/capturemode.cgi', params=params, auth=HTTPDigestAuth(self.__username, self.__password))

    def dynamic_overlay(self, params=None, json=None):
        return requests.post(self.base_url + f'axis-cgi/dynamicoverlay/dynamicoverlay.cgi', params=params, json=json, auth=HTTPDigestAuth(self.__username, self.__password))
