import requests
import json
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://10.10.5.163:8020'
HEADERS = {'content-type': 'application/json'}


class Credentials(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Login(Credentials):
    def __init__(self, username, password):
        Credentials.__init__(self, username, password)
        self.login_url = BASE_URL + '/api/login/'

    def login_user(self):
        try:
            r = requests.get(self.login_url, auth=HTTPBasicAuth(self.username, self.password))
            print(r.json())
        except requests.RequestException as e:
            r = e
            print(r)
        return r


class Register:
    def __init__(self):
        self.register_url = BASE_URL + '/open/signup'
        self.register_otp_url = BASE_URL + '/open/activate'

    def register_user(self, data_dict):
        try:
            r = requests.post(self.register_url, data=json.dumps(data_dict), headers=HEADERS)
        except requests.RequestException as e:
            r = e
        print(r)
        return r

    def register_otp(self, data_dict):
        try:
            r = requests.post(self.register_url, data=json.dumps(data_dict), headers=HEADERS)
        except requests.RequestException as e:
            r = e
        print(r)
        return r
