from telegram.ext import Updater


# Method should return json with true/false flag and message
def rule_1(balance_o, balance_n):
    # Here could be any condition
    return {
        'flag': True if (float(balance_o) != float(balance_n)) else False,
        'msg': 'Old balance: {0} ETH\nNew balance: {1} ETH\nDelta: {2} ETH'
        .format(
            str(float(balance_o) / 1000000000000000000),
            str(float(balance_n) / 1000000000000000000),
            str(abs(float(balance_n) / 1000000000000000000 - float(balance_o) / 1000000000000000000)))
    }


def rule_2(balance_o, balance_n):
    # Here could be any condition
    balance_o = float(balance_o)/1000000000000000000
    balance_n = float(balance_n)/1000000000000000000
    return {
        'flag': True if (abs(balance_o - balance_n) >= 1.0) else False,
        'msg': 'BALANCE: {0} ETH'.format(balance_n)
    }


def send(token, chat_id, text):
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=token)

    # Send single message (no bot looping)
    updater.bot.send_message(chat_id=chat_id, text=text)
