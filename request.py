import requests
from auth import api_key
import json

class Request:
    def __init__(self):
        self.api_key = api_key
    @staticmethod
    def get_content(url, param):
        response = requests.get(url, params=param)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            print(f"Request completed with Error. Response Code : {response.status_code}")
            return None