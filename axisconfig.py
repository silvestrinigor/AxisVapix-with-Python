import requests
from requests.auth import HTTPDigestAuth

class AxisCam:
    
    def _init_(self, ip, password, username, method, cgi, data, port):
        self.ip = ip
        self.username = username
        self.password = password
        self.method = method
        self.cgi = cgi
        self.data = data
        self.port = port
   
    def axis_cam (self):
        
        if method == 'get':
            print (f'http://{ip}:{port}/axis-cgi/{cgi}')
            r =  requests.get (f'http://{ip}:{port}/axis-cgi/{cgi}', auth=HTTPDigestAuth(f'{username}',f'{password}'), timeout=1)
            print(r.text)
            return r
        if method == 'post':
            print (f'http://{ip}:{port}/axis-cgi/{cgi}')
            r = requests.post (f'http://{ip}:{port}/axis-cgi/{cgi}', auth=HTTPDigestAuth(f'{username}',f'{password}'), json=data, timeout=1)
            print(r.text)
            return r

ip = "192.168.0.90"
username = "root"
password = "pass"
port = "80"
cgi = "basicdeviceinfo.cgi"
method = "post"
data ={
    "apiVersion": "1.0",
    "context": "Client defined request ID",
    "method": "getAllProperties"
}

a = AxisCam(ip,password, username, method, cgi, data, port)
print(a.axis_cam())