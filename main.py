import PySimpleGUI as sg
import requests

API_URL = "https://en.wiktionary.org/api/rest_v1/page/definition/{}"


def get_german_title_tags(word: str):
    """Return a list of part-of-speech tags for the German entry of a word."""
    url = API_URL.format(word)
    response = requests.get(url, headers={"User-Agent": "FlashcardApp/1.0"})

    if response.status_code != 200:
        return None  # word not found or API error

    data = response.json()
    german_entries = []

    # data is a dict: { "de": [...], "sv": [...], "other": [...], ... }
    for lang_code, entries in data.items():
        if not isinstance(entries, list):
            continue

        for entry in entries:
            language_name = entry.get("language", "")
            if "German" in language_name:
                german_entries.append({
                    "lang_code": lang_code,
                    "language": language_name,
                    "partOfSpeech": entry.get("partOfSpeech"),
                    "definitions": entry.get("definitions", [])
                })

    return german_entries[0]["definitions"][0]


def main():
    layout = [
        [sg.Text("German Flashcards", font=("Arial", 20))],
        [sg.Text("Word:"), sg.Text("", key="-WORD-")],
        [sg.Button("Show Answer")], [sg.Button("Next"), sg.Button("Exit")]
    ]

    window = sg.Window("Flashcards", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "Next":
            window["-WORD-"].update(get_german_title_tags("hund"))  # placeholder

        if event == "Show Answer":
            sg.popup("Answer: das Haus (neuter)")

    window.close()

if __name__ == "__main__":
    main()

