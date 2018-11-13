import sys
import json

sys.path.insert(0, '..')
sys.path.insert(0, '../..')

from src.config.live import PARAMS, TOKEN, CHAT_ID
from src import telega
from src.search_by import SearchBy as sb


def read_file():
    with open('data.json', 'r') as income:
        result = json.load(income)
    return result


def write_file(result):
    with open('data.json', 'w') as outcome:
        json.dump(result, outcome)


if __name__ == '__main__':

    data = {}

    try:

        # get remote http data
        for item in PARAMS:
            data[item['name']] = sb.parse(item['search_by'], **item)

        # read data from local file
        old_data = read_file()

        # Send msg to telegram if data is updated
        rule = telega.rule_1(
            old_data['balance']['result'],
            data['balance']['result']
        )
        if rule['flag']:
            telega.send(TOKEN, CHAT_ID, rule['msg'])

        # rule = telega.rule_2(
        #     old_data['balance']['result'],
        #     data['balance']['result']
        # )
        # if rule['flag']:
        #     telega.send(TOKEN, CHAT_ID, rule['msg'])

        # update old data to new one in local file
        write_file(data)

    except Exception as err:
        print(err)
