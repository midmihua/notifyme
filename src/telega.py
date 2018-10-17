from telegram.ext import Updater


# Method should return json with true/false flag and message
# Example 1
def rule_1(balance, userDividendsWei):
    # Here could be any condition
    return {
        'flag': True if (float(balance) > 0 and float(userDividendsWei) > 0) else False,
        'msg': 'balance: {0}; userDividendsWei: {1}'.format(balance, userDividendsWei)
    }


# Example 2
def rule_2(balance, userDividendsWei):
    # Here could be any condition
    return {
        'flag': True if float(balance) <= float(userDividendsWei) else False,
        'msg': 'balance: {0} <= userDividendsWei: {1}'.format(balance, userDividendsWei)
    }


# Example 3
def rule_3(balance, userDividendsWei):
    # Here could be any condition
    return {
        'flag': True if float(balance) > float(userDividendsWei) else False,
        'msg': 'balance: {0} > userDividendsWei: {1}'.format(balance, userDividendsWei)
    }


def send(token, chat_id, text):
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=token)

    # Send single message (no bot looping)
    updater.bot.send_message(chat_id=chat_id, text=text)
