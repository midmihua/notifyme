from telegram.ext import Updater


def send(token, chat_id, text):
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=token)

    # Send single message (no bot looping)
    updater.bot.send_message(chat_id=chat_id, text=text)
