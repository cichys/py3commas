# py3commas [![PyPI version](https://badge.fury.io/py/py3commas.svg)](https://badge.fury.io/py/py3commas)
Unofficial Python wrapper for the [3Commas API](https://github.com/3commas-io/3commas-official-api-docs)

W.I.P.

How to install 

```bash
pip install py3commas
```

How to use

```python
from py3commas.request import Py3Commas

p3c = Py3Commas(key='', secret='')
response = p3c.request(
    domain='smart_trades',
    name=''
)
response = p3c.request(
    domain='smart_trades', 
    name='create_smart_trade', 
    payload={
        "account_id": 123456
    }
)
```