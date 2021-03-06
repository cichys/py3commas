import pytest
from .request import Py3Commas


def test_error_missing_key():
    with pytest.raises(ValueError) as excinfo:
        assert Py3Commas(
            key='',
            secret='mysupersecret'
        )
    excinfo.match(r'Missing key')


def test_error_missing_secret():
    with pytest.raises(ValueError) as excinfo:
        assert Py3Commas(
            key='mykey',
            secret=''
        )
    excinfo.match(r'Missing secret')


def test_error_missing_entity():
    p3c = Py3Commas(
        key='mykey',
        secret='mysupersecret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3c.request('', '')
    excinfo.match(r'Missing entity')


def test_error_invalid_entity():
    p3c = Py3Commas(
        key='mykey',
        secret='mysupersecret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3c.request('test', '')
    excinfo.match(r'Invalid entity')


def test_error_invalid_action():
    p3c = Py3Commas(
        key='mykey',
        secret='mysupersecret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3c.request('smart_trades', 'test')
    excinfo.match(r'Invalid action')


def test_error_missing_id():
    p3c = Py3Commas(
        key='mykey',
        secret='mysupersecret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3c.request('smart_trades', 'step_panic_sell')
    excinfo.match(r'Missing id')
    with pytest.raises(ValueError) as excinfo:
        assert p3c.request('smart_trades', 'step_panic_sell', '')
    excinfo.match(r'Missing id')