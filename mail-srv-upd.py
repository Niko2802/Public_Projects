import tkinter as tk

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
    for i in list_ch_boxes:
        print(i.get_value())


window = tk.Tk()
window.title("Заявка в ИТ")
window.geometry("500x500")

subject_label = tk.Label(window, text="Тема письма:")
subject_label.grid(row=0, column=0)

subject = tk.Text(window, height=3, width=50)
subject.grid(row=1, column=0, rowspan=3, columnspan=5)

list_ch_boxes = []
for i in factory:
    list_ch_boxes.append(Ch_box(window, i, 4 + factory.index(i), 0))

button_send = tk.Button(window, text="Отправить", command=on_button_send_click)
button_send.grid(row=15, column=0)



window.mainloop()