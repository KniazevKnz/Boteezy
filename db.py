from pymongo import MongoClient
import settings

client = MongoClient(settings.MONGO_LINK)

db = client[settings.MONGO_DB]


def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({"user_id": effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id
        }
        db.users.insert_one(user)
    return user


def subscribe_user(db, user_data):
    if not user_data.get('subscribed'):
        db.users.update_one(
            {'_id': user_data['_id']},
            {'$set': {'subscribed': True}}
        )


def unsubscribe_user(db, user_data):
    db.users.update_one(
        {'_id': user_data['_id']},
        {'$set': {'subscribed': False}}
    )


def get_subscribed(db):
    return db.users.find({"subscribed": True})


def get_or_add_channels(db, user_data, channels):
    if not user_data.get('channels'):
        db.users.update_one(
            {'_id': user_data['_id']},
            {'$set': {'channels': channels}}
        )
    else:
        db.users.update_one(
            {'_id': user_data['_id']},
            {'$set': {'channels': channels}}
        )


def write_post(db, message, date, edit_date):
    post = db.cha.find_one({"date": date})
    if not post:

        post = {
            "channel_name": settings.CHANNEL_NAME,
            "post": message,
            "date": date,
            "edit_date": edit_date,
            "delete": False,
            "notification": False
            }
        db.cha.insert_one(post)


def get_posts(db):
    return db.cha.find()


def find_post(db, date):
    return db.cha.find_one({"date": date})


def set_delete_flag(db, date):
    db.cha.update_one(
            {"date": date},
            {'$set': {'delete': True}}
        )


def check_deleted(db):
    post = db.cha.find({"delete": True})
    return post


def notification_flag(db, date):
    db.cha.update_one(
            {"date": date},
            {'$set': {'notification': True}}
        )
