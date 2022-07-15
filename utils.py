from telegram import ReplyKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup([
        ['/start', '/subscribe', '/unsubscribe', '/check']
    ])
