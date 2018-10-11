"""
Live configuration
"""

# Remote resource section
BASE_REMOTE_URL = 'https://api.coinmarketcap.com/v2/ticker/'

# Telegram section
TOKEN = 'provide_real_token'
CHAT_ID = 'provide_real_chat_id'

# Necessary params to gather the data
PARAMS = [
    {
        'name': 'BTC',
        'url': 'https://api.coinmarketcap.com/v2/ticker/1/',
        'desc': 'Bitcoin',
        'price': 'data.quotes.USD.price'
    },
    {
        'name': 'LTC',
        'url': 'https://api.coinmarketcap.com/v2/ticker/2/',
        'desc': 'Litecoin',
        'price': 'data.quotes.USD.price'
    }
]
