API_URL = 'https://api.3commas.io'
API_VERSION = '/public/api/ver1/'

APIS = {
    'smart_trades': {
        '': ('GET', ''),
        'step_panic_sell': ('POST', '{id}/step_panic_sell'),
        'update': ('POST', '{id}/update')
    }
}