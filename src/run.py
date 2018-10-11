import requests as r

import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../..')

from src.config.debug import PARAMS, BASE_REMOTE_URL, TOKEN, CHAT_ID
from src import telega


# Read and set up configuration
def get_url(url_local, url_base):
    return url_local if len(url_local) > 0 else url_base


# Request the data
def get_remote_data(url):
    return r.get(url).json()


# Get specific value
def get_value(path, data=None):
    path = path.split('.')
    if len(path) > 0 and data is not None:
        for it in path:
            data = data[it]
    return data


if __name__ == '__main__':

    msg = str()

    for item in PARAMS:
        print(item)
        url = get_url(item['url'], BASE_REMOTE_URL)
        msg += 'Price of {0} is {1}\n'.format(
            item['name'],
            get_value(item['price'], get_remote_data(url))
        )
        print(msg)

    # Send msg to telegram
    telega.send(TOKEN, CHAT_ID, msg)
