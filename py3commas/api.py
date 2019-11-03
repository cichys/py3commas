import hashlib
import hmac
from .config import API_URL


class Api:
    def __init__(self, key: str, secret: str):
        self.url = API_URL
        self.key = key
        self.secret = secret

    def generate_signature(self, uri: str, data: str) -> str:
        pass

    def make_request(self, path: str, params: any):
        pass
