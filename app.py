import PySimpleGUI as sg

def main():
    layout = [
        [sg.Text("German Flashcards", font=("Arial", 20))],
        [sg.Text("Word:"), sg.Text("", key="-WORD-")],
        [sg.Button("Show Answer"), sg.Button("Next"), sg.Button("Exit")]
    ]

    window = sg.Window("Flashcards", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "Next":
            window["-WORD-"].update("Haus")  # placeholder

        if event == "Show Answer":
            sg.popup("Answer: das Haus (neuter)")

    window.close()

if __name__ == "__main__":
    main()
