import hashlib
import hmac
import requests
import json
from .config import API_URL, API_VERSION, APIS


class Py3Commas:

    def __init__(self, key: str, secret: str):
        if key is None or key == '':
            raise ValueError('Missing key')
        if secret is None or secret == '':
            raise ValueError('Missing secret')

        self.key = key
        self.secret = secret

    def _generate_signature(self, path: str, data: str) -> str:
        byte_key = str.encode(self.secret)
        message = str.encode(API_VERSION + path + data)
        signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
        return signature

    def _make_request(self, http_method: str, path: str, params: any, payload: any):
        signature = self._generate_signature(path, params)

        response = requests.request(
            method=http_method,
            url=API_URL + API_VERSION + path + '?' + params,
            headers={
                'APIKEY': self.key,
                'Signature': signature
            },
            data=payload
        )
        return json.loads(response.text)

    def request(self, domain: str, name: str = '', _id: str = None, payload: any = None):
        if domain is None or domain == '':
            raise ValueError('Missing domain')
        if domain not in APIS:
            raise ValueError('Invalid domain')
        if name not in APIS[domain]:
            raise ValueError('Invalid api')

        api = APIS[domain][name]
        api_path = api[1]
        if '{id}' in api_path:
            if _id is None or _id == '':
                raise ValueError('Missing id')
            api_path = api_path.replace('{id}', _id)

        return self._make_request(
            http_method=api[0],
            path=domain + api_path,
            params='',
            payload=payload
        )
