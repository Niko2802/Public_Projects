import tkinter as tk
from tkinter import messagebox
from exchangelib import Credentials, DELEGATE, Account, Configuration, Message, Mailbox


credentials = Credentials(username='NEW_TN\\simakov', password='MoskaliPidarasy14')
config = Configuration(server='mail.tn.ru', credentials=credentials)
my_account = Account(
    primary_smtp_address='simakov@nicol-pack.ru', config=config,
    autodiscover=False, access_type=DELEGATE
)
to_recipients = ["simakov@nicol-pack.ru"]
factory = ["агтф", "уз", "тн-юг", "в", "м", "мф", "нн", "тн-нн", "ну", "ук", "уч"]

class Ch_box():
    def __init__(self, window, name, row, col):
        self.name = name
        self.value = tk.BooleanVar()
        self.ch_box = tk.Checkbutton(window, text=name, variable=self.value)
        self.ch_box.grid(row=row, column=col, sticky="w")

    def get_value(self):
        return self.value.get()


def on_button_send_click():
    subj = ""
    if selected_option.get() == "":
        subj = subject.get("1.0", tk.END)
    elif subject.get() == "":
        subj = selected_option.get()
    else:
        messagebox.showwarning(title="Warning", message="This is a warning message!")
    for i in list_ch_boxes:
        if i.get_value():
            print(i.name, i.get_value())
            print(selected_option.get())
            Message(account=my_account, to_recipients=to_recipients,
                    subject=f"{i.name} {subj}", body=subj).send()


window = tk.Tk()
window.title("Заявка в ИТ")
window.geometry("500x500")

subject_label = tk.Label(window, text="Тема письма:")
subject_label.grid(row=0, column=0)

subject = tk.Text(window, height=3, width=50)
subject.grid(row=1, column=0, rowspan=3, columnspan=5)

selected_option = tk.StringVar()
options = ["Установка обновлений на сервера", "Провилактика сервера", "Настройка коммутатора"]
option_menu = tk.OptionMenu(window, selected_option, *options)
option_menu.grid(row=4, column=0, columnspan=3)


list_ch_boxes = []
for i in factory:
    list_ch_boxes.append(Ch_box(window, i, 5 + factory.index(i), 0))

button_send = tk.Button(window, text="Отправить", command=on_button_send_click)
button_send.grid(row=16, column=0)



window.mainloop()