import random
import string
from netmiko import ConnectHandler
import imaplib
import smtplib
import email
import schedule
import time
import logging
from email.message import EmailMessage


pass_wifi = 0
logging.basicConfig(level=logging.INFO, filename="wifi-guest.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")

def generate_password(length=8):
    characters = string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def create_user_wlc(wlc, pass_wifi="1122334455", host=""):
    net_connect = ConnectHandler(**wlc)
    on_connect = net_connect.find_prompt()
    if on_connect == "(Cisco Controller) >":
        logging.info("Связь с контроллером установлена")
    else:
        logging.error("Ошибка при установке связи с контроллером")
    wlan_str = net_connect.send_command("show wlan summary")
    list_tmp = wlan_str.split("\n")
    for i in list_tmp:
        i = i.lower()
        if i.find("4clips-guest") != -1:
            wlan_id = i[0]
    send_res_dis = net_connect.send_command("config wlan disable 4")
    if send_res_dis == "" or send_res_dis == "\n":
        logging.info("WiFi сеть 4clips-guest отключена")
    else:
        logging.error(f"Ошибка при отключении WiFi сети 4clips-guest, текст ошибки: {send_res_dis}")
    send_res_pass = net_connect.send_command(f"config wlan security wpa akm psk set-key ascii {pass_wifi} {wlan_id}")
    if send_res_pass == "" or send_res_dis == "\n":
        logging.info("Пароль для WiFi 4clips-guest установлен")
    else:
        logging.error(f"Ошибка при установке пароля для WiFi 4clips-guest {send_res_pass}")
    send_res_en = net_connect.send_command("config wlan enable 4")
    if send_res_en == "" or send_res_dis == "\n":
        logging.info("WiFi сеть 4clips-guest включена")
    else:
        logging.error(f"Ошибка при включении WiFi сети 4clips-guest {send_res_en}")
    net_connect.save_config()
    logging.info("Конфигурация контроллера сохранена")
    net_connect.disconnect()
    logging.info("Соединение с контроллером разорвано")
    return


def send_mail(pass_wifi):
    mail = imaplib.IMAP4_SSL("imap.yandex.ru")
    res_conn_mail = mail.login("helpdesk-1@4clips.ru", "lwlxwratgncopvtu")
    if res_conn_mail[0] == "OK":
        logging.info("Успешное подключение к ящику")
    else:
        logging.error("Ошибка при подключении к ящику")
    mail.list()
    mail.select("WiFi")
    result, data = mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    for i in id_list:
        result, data = mail.fetch("1", "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode("utf-8")
        email_message = email.message_from_string(raw_email_string)
        from_user = email.utils.parseaddr(email_message["From"])
        addr_user = from_user[1]
        addr_user_domain = addr_user.split("@")[1]
        if addr_user_domain == "4clips.ru":
            mail_send = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
            mail_send.login("helpdesk-1@4clips.ru", "lwlxwratgncopvtu")
            msg = EmailMessage()
            msg['Subject'] = "Пароль для WiFi 4clips-guest"
            msg['From'] = "wifi@4clips.ru"
            msg['To'] = addr_user
            msg.set_content(f"Пароль для WiFi 4clips-guest: {pass_wifi}")
            mail_send.sendmail("helpdesk-1@4clips.ru", addr_user, msg.as_string())
            mail_send.quit()
            mail.store("1", "+FLAGS", "\\Deleted")
            mail.expunge()
            logging.info(f"Пароль был выслан на адрес {addr_user}")
        else:
            logging.info(f"Получено письмо от неавторизованного пользователя {addr_user}")
            mail.store("1", "+FLAGS", "\\Deleted")
            mail.expunge()
    return


def job():
    schedule.cancel_job(send_mail)
    global pass_wifi
    pass_wifi = generate_password()
    devices = {
        "Cisco_db:30:84": "10.96.20.5",
        }
    for host_name in devices:
        device = {
            "device_type": "cisco_wlc",
            "host": devices[host_name],
            "username": "simakov",
            "password": "28fev1980M07",
        }
        create_user_wlc(device, pass_wifi, host_name)
    schedule.every(30).seconds.do(send_mail, pass_wifi)
    return pass_wifi


logging.info("Прошрамма запущена")

pass_wifi = job()
logging.info(f"Пароль для WiFi 4clips-guest установлен: {pass_wifi}")

schedule.every().day.at("03:00").do(job)
logging.info("Создано задание на смену пароля раз в сутки в 03:00")

while True:
    schedule.run_pending()
    time.sleep(1)
