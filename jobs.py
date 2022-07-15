from db import db, check_deleted, notification_flag, get_subscribed


def check_deleted_posts(context):
    for user in get_subscribed(db):
        context.bot.send_message(chat_id=user['chat_id'], text='Проверяю удаленные посты')
        deleted_posts = check_deleted(db)
        for post in deleted_posts:
            if post['notification'] is False:
                post_message = post['post']
                post_date = post['date']
                channel = post['channel_name']
                context.bot.send_message(chat_id=user['chat_id'], text=f'Пост {post_message} в канале {channel} от {post_date} удален')
                notification_flag(db, post['date'])

