# Boteezy

Boteezy - это бот который уведомляет об удалении постов с Telegram канала.

## Установка

Скачайте проект с github и установите зависимости:

```
git clone https://github.com/KniazevKnz/Boteezy.git
```

Создайте виртуальное окружение и установите зависимости:
```
pip install -r requirements.txt
```

Создайте файл settings.py и задайте в нем базовые переменные:
```
API_KEY = ""  API ключ для бота
PROXY_URL = "" URL прокси сервера если используется
PROXY_USERNAME = "" Логин прокси сервера
PROXY_PASSWORD = "" Пароль прокси сервера
MONGO_LINK = "" Ссыллка на базу данных MongoDb
MONGO_DB = "" Название базы данных в MongoDb
API_ID = "" API ID для парсера постов Telegram
API_HASH = "" API HASH для парсера постов Telegram
LOG_PHONE = "" Номер телефона для аккаунта который будет заходить на каналы для парсинга постов
CHANNEL_NAME = "" Название канала который необходимо парсить
```

## Запуск программы
Для запуска программы запустите файлы 'bot.py' и 'postparser.py' параллельно
