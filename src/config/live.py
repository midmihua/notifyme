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
        'url': 'https://api.etherscan.io/api?module=account&action=balance&address=0xAC99580f92Eb7a91daFf30de133F93aD82b5070a',
        'param': 'result',
        'search_by': 1
    }
]
