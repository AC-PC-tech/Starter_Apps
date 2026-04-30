import PySimpleGUI as sg

layout = [
    [sg.Text("PySimpleGUI is working!")],
    [sg.Button("OK")]
]

window = sg.Window("Test Window", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "OK":
        break

window.close()
