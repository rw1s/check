from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID","21758907")
APP_HASH = os.environ.get("APP_HASH","8706012edc2aba4f107099c070a0fee7")
BOT_USERNAME = os.environ.get("BOT_USERNAME","حيدر")
session = os.environ.get("TERMUX","1BJWap1wBu7J7qaXAhmS9GUS_qMVXuD9k-ZLTajFfp1aBGd_3RgNjOJD-KxMgGM8xLAmpd7AVFhaXOYk12GQ7kWmluZaossK7xty8as9jlC1jliGUW6EgHcGmeeyUTYnmS1q2Zvuh8FEo79WjT2_6QQN8M6RZeZwjU9s4bu4JlDbzRKai2WlJZKvZpbuY3fENqGIQLMNTkiWMlnplrkBaYYpRfmoqKWKfoK5KzRgXQVzxcUiE_PfLCOl2Y6wSG4kovtj58mtHcp3G6FWdgyGOT8y1Bux79KNl6ZZzxeOlYcdTEAcL4wzDDBJVdZf31mo5V4TaX8VGX5pAh5BRKHz7qavuv3HrPHs=")
SESSION = os.environ.get("TERMUX","1BJWap1wBu7J7qaXAhmS9GUS_qMVXuD9k-ZLTajFfp1aBGd_3RgNjOJD-KxMgGM8xLAmpd7AVFhaXOYk12GQ7kWmluZaossK7xty8as9jlC1jliGUW6EgHcGmeeyUTYnmS1q2Zvuh8FEo79WjT2_6QQN8M6RZeZwjU9s4bu4JlDbzRKai2WlJZKvZpbuY3fENqGIQLMNTkiWMlnplrkBaYYpRfmoqKWKfoK5KzRgXQVzxcUiE_PfLCOl2Y6wSG4kovtj58mtHcp3G6FWdgyGOT8y1Bux79KNl6ZZzxeOlYcdTEAcL4wzDDBJVdZf31mo5V4TaX8VGX5pAh5BRKHz7qavuv3HrPHs=")
token = os.environ.get("TOKEN","5909477203:AAGOMUqsZGJjO0TocHT9uiiyXjTciqTBkp4")
sosta = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
