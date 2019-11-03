import hashlib
import hmac
import requests
from .config import API_URL, API_URL_PATH


class Api:

    def __init__(self, key: str, secret: str):
        self.url = API_URL
        self.url_path = API_URL_PATH
        self.key = key
        self.secret = secret

    def generate_signature(self, path: str, data: str) -> str:
        total_params = self.url_path + path + data
        byte_key = str.encode(self.secret)
        message = str.encode(total_params)
        signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
        return signature

    def make_request(self, path: str, params: any):
        signature = self.generate_signature(path, params)

        response = requests.get(
            self.url + self.url_path + path + '?' + params,
            headers={
                'APIKEY': self.key,
                'Signature': signature
            }
        )
        return response
