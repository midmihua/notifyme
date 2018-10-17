"""
Live configuration
"""

# Telegram section
TOKEN = 'provide-token'
CHAT_ID = 'provide-chat-id'

# Necessary params to gather the data
PARAMS = [
    {
        'name': 'balance',
        'url': 'https://api.etherscan.io/api?module=account&action=balance&address=0xb10ea0d397db942a1083a4af9c6074ab63bc8c8b',
        'param': 'result',
        'search_by': 1

    },
    {
        'name': 'userDividendsWei',
        'url': 'https://etherscan.io/readContract?a=0xb10ea0d397db942a1083a4af9c6074ab63bc8c8b&v=0xb10ea0d397db942a1083a4af9c6074ab63bc8c8b',
        '_address': '0x168a71D66255c6fdB70418Ec0d0100920C57333e',
        'delay': 3,
        'search_by': 2
    }
]
