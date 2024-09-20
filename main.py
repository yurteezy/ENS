import telegram_bot
import user_interface
import asyncio
import pandas as pd

contacts_path = "/Users/appletrh/PycharmProjects/ENS/contacts.csv"

df = pd.read_csv(contacts_path, delimiter=';')
contacts_list = df.to_dict(orient='records')

# Fetch the message and selected services from the user interface
services, message = user_interface.get_alert()

if message and services:
    for contact in contacts_list:
        if 'Telegram' in services:
            chat = contact.get("Telegram")
            print(f"Sending message to {contact['Name']} via Telegram (ID: {chat})")
            try:
                asyncio.run(telegram_bot.send_startup_message(chat, message))
            except Exception as e:
                print(f"Failed to send message to {contact['Name']}: {e}")