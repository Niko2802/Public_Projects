import tkinter as tk

factory = ["агтф", "уз", "тн-юг", "в", "м", "мф", "нн", "тн-нн", "ну", "ук", "уч"]

def on_button_send_click():
    pass

window = tk.Tk()
window.title("Заявка в ИТ")
window.geometry("500x500")

subject_label = tk.Label(window, text="Тема письма:")
subject_label.grid(row=0, column=0)

subject = tk.Text(window, height=3, width=50)
subject.grid(row=1, column=0, rowspan=3, columnspan=5)


for i in factory:
    cb_val = tk.BooleanVar()
    cb = tk.Checkbutton(window, text=i, variable=cb_val)
    cb.grid(row=4 + factory.index(i), column=0, sticky="w")


button_send = tk.Button(window, text="Отправить", command=on_button_send_click)
button_send.grid(row=15, column=0)



window.mainloop()