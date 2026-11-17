
import requests
import constant as constant
from utils.api import api_helper


class APIClient:
    def __init__(self, base_url=None, headers = None, proxies=None):
        self.base_url = base_url
        self.headers = headers
        self.proxies = proxies 
    
    def post(self, endpoint, parameter=None, payload=None, payload_type = "json"):
        url = api_helper.construct_url(self.base_url, endpoint, parameter)
        request_args = {
        "headers": self.headers,
        "proxies": self.proxies,
        "verify": False
        }
        if payload is not None:
            request_args[payload_type] = payload
        return requests.post(url, **request_args)
    
    def get(self, endpoint, parameter=None):
        url = api_helper.construct_url(self.base_url, endpoint, parameter)
        return requests.get(url, headers=self.headers, proxies=self.proxies,verify=False)