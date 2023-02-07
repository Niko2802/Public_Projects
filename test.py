import PySimpleGUI as sg
layout = [
    [sg.Button('Coffee-1', size=(15, 1)), sg.Text('100 рублей', size=(15, 1))],
    [sg.Button('Coffee-2', size=(15, 1)), sg.Text('200 рублей', size=(15, 1))],
]
window = sg.Window('Кофе машина', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break