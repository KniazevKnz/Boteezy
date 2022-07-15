import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (greet_user, talk_to_me, subscribe, unsubscribe, add_channels)
import settings
from jobs import check_deleted_posts

logging.basicConfig(filename="bot.log", level=logging.INFO)
# delete "#" if you want use proxy
# PROXY = {'proxy_url': settings.PROXY_URL,
#    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME,
# 'password': settings.PROXY_PASSWORD}}


def main():

    mybot = Updater(settings.API_KEY, use_context=True)

    jq = mybot.job_queue
    jq.run_repeating(check_deleted_posts, interval=10, first=0)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("subscribe", subscribe))
    dp.add_handler(CommandHandler("unsubscribe", unsubscribe))
    dp.add_handler(CommandHandler("add_channels", add_channels))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

