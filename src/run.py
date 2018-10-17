import sys

sys.path.insert(0, '..')
sys.path.insert(0, '../..')

from src.config.debug import PARAMS, TOKEN, CHAT_ID
from src import telega
from src.search_by import SearchBy as sb

if __name__ == '__main__':

    data = {}

    for item in PARAMS:
        print(item)
        data[item['name']] = sb.parse(item['search_by'], **item)

    print(data)

    # Send msg to telegram
    # Example 1
    r1 = telega.rule_1(data['balance']['result'], data['userDividendsWei']['result'])
    if r1['flag']:
        telega.send(TOKEN, CHAT_ID, r1['msg'])

    # Example 2
    r2 = telega.rule_2(data['balance']['result'], data['userDividendsWei']['result'])
    if r2['flag']:
        telega.send(TOKEN, CHAT_ID, r2['msg'])

    # Example 3
    r3 = telega.rule_3(data['balance']['result'], data['userDividendsWei']['result'])
    if r3['flag']:
        telega.send(TOKEN, CHAT_ID, r3['msg'])
