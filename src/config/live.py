"""
Live configuration
"""

# Telegram section
TOKEN = '701851601:AAGOsJShMexjzBKrxdsa6XYy0CAGH4OB-t4'
CHAT_ID = '493097614'

# Necessary params to gather the data
PARAMS = [
    {
        'name': 'balance',
        'url': 'https://api.etherscan.io/api?module=account&action=balance&address=0xb10ea0d397db942a1083a4af9c6074ab63bc8c8b',
        'param': 'result',
        'search_by': 1
    }
]
