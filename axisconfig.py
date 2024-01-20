import requests
from requests.auth import HTTPDigestAuth

class AxisCam:
    
    def __init__(self, ip, password, username, method, cgi, data, port):
        self.ip = ip
        self.username = username
        self.password = password
        self.method = method
        self.cgi = cgi
        self.data = data
        self.port = port
   
    def axis_cam (self):
        
        if self.method == 'get':
            print (f'http://{self.ip}:{self.port}/axis-cgi/{self.cgi}')
            r =  requests.get (f'http://{self.ip}:{self.port}/axis-cgi/{self.cgi}', auth=HTTPDigestAuth(f'{self.username}',f'{self.password}'), timeout=1)
            print(r.text)
            return r
        if self.method == 'post':
            print (f'http://{self.ip}:{self.port}/axis-cgi/{self.cgi}')
            r = requests.post (f'http://{self.ip}:{self.port}/axis-cgi/{self.cgi}', auth=HTTPDigestAuth(f'{self.username}',f'{self.password}'), json=self.data, timeout=1)
            print(r.text)
            return r
