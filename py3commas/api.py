import hashlib
import hmac
import binascii
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
        byte_key = binascii.unhexlify(self.secret)
        message = total_params.encode()
        signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
        print("signature = {0}".format(signature))
        return signature

    def make_request(self, path: str, params: any):
        signature = self.generate_signature(path, params)

        response = requests.get(
            self.url + self.url_path + path,
            headers={
                'APIKEY': self.key,
                'Signature': signature
            }
        )
        return response

