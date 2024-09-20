import requests
import telegram
import asyncio

token = "7792328835:AAH1N9IuA4ftWnhuQBGIEkbXZs_rBMRd2bE"
# url = f"https://api.telegram.org/bot{token}/getUpdates"
# print(requests.get(url).json())
user_id = "1170057607"
bot = telegram.Bot(token)


async def send_startup_message(user, notification):
    await bot.send_message(chat_id=user, text=notification)

