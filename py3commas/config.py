API_URL = 'https://api.3commas.io'
API_VERSION = '/public/api/ver1/'

APIS = {
    'smart_trades': {
        'create_simple_sell': ('POST', 'create_simple_sell'),
        'create_simple_buy': ('POST', 'create_simple_buy'),
        'create_smart_sell': ('POST', 'create_smart_sell'),
        'create_smart_cover': ('POST', 'create_smart_cover'),
        'create_smart_trade': ('POST', 'create_smart_trade'),
        '': ('GET', ''),
        'cancel_order': ('POST', '{id}/cancel_order'),
        'add_funds': ('POST', '{id}/add_funds'),
        'step_panic_sell': ('POST', '{id}/step_panic_sell'),
        'update': ('POST', '{id}/update'),
        'cancel': ('POST', '{id}/cancel'),
        'panic_sell': ('POST', '{id}/panic_sell'),
        'force_process': ('POST', '{id}/force_process'),
    }
}