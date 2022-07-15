from db import (db, get_or_create_user, subscribe_user, unsubscribe_user, get_or_add_channels)
from utils import main_keyboard


def greet_user(update, context):
    get_or_create_user(db, update.effective_user, update.message.chat.id)
    print("Вызван /start")
    update.message.reply_text('Здравствуй, пользователь!',  reply_markup=main_keyboard())


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text}',  reply_markup=main_keyboard())


def subscribe(update, context):
    user = get_or_create_user(db, update.effective_user, update.message)
    subscribe_user(db, user)
    update.message.reply_text('Вы подписались',  reply_markup=main_keyboard())


def unsubscribe(update, context):
    user = get_or_create_user(db, update.effective_user, update.message)
    unsubscribe_user(db, user)
    update.message.reply_text('Вы отписались', reply_markup=main_keyboard())


def add_channels(update, context):
    user = get_or_create_user(db, update.effective_user, update.message)
    channels = update.message.text
    print(channels)
    channels_list = channels.split(' ')
    print(channels_list[1:-1])
    get_or_add_channels(db, user, channels_list)
    update.message.reply_text(f'Вы успешно добавили каналы {channels_list[1:-1]}', reply_markup=main_keyboard())

