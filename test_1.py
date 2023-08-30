import requests
import string
import random
import os
import iuliia

source = "Харитон"
trans = iuliia.translate(source, schema=iuliia.WIKIPEDIA)
print(trans)


def change_password_current_user(new_password):
    os.system(f"net user /password:{new_password}")


def generate_password(length, complexity=2):
    if complexity == 1:
        characters = string.digits
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = 8
complexity = 2
password = generate_password(length, complexity)
print(password)


def send_message_to_telegram(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage?&chat_id={chat_id}&text={text}'
    # url1 = f"https://api.telegram.org/bot{token}/getUpdates"
    # print(requests.get(url1).json())
    response = requests.get(url)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message", response.status_code)


token = "6127996240:AAEx7ZVnnUyarPpU0mTTCHx01KGW2nMEbWw"
chat_id = "-1001714960360"
text = f"Новый пароль на игры: {password}"
send_message_to_telegram(token, chat_id, text)
