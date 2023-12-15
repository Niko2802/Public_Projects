import tkinter as tk


def on_button_send_click():
    print("Отправка...")
    print(cb_nn_val.get())
    print("Отправка...")


window = tk.Tk()
window.title("Заявка в ИТ")
window.geometry("500x500")

subject_label = tk.Label(window, text="Тема письма:")
subject_label.grid(row=0, column=0)

subject = tk.Text(window, height=3, width=50)
subject.grid(row=1, column=0, rowspan=3, columnspan=5)

cb_nn_val = tk.BooleanVar()
cb_nn = tk.Checkbutton(window, text="нн.", variable=cb_nn_val)
cb_nn.grid(row=4, column=0)

cb_uk_val = tk.BooleanVar()
cb_uk = tk.Checkbutton(window, text="ук.", variable=cb_uk_val)
cb_uk.grid(row=4, column=1)

button_send = tk.Button(window, text="Отправить", command=on_button_send_click)
button_send.grid(row=6, column=0)



window.mainloop()