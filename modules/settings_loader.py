import json
import os

def load_settings():
    with open(os.path.expanduser("~") + "/.config/pinboard/settings.json") as file:
        settings = json.load(file)

    return settings

def change_window(canvas, root):
    settings = load_settings()

    canvas.config(highlightbackground=settings['border_color'])
    canvas.config(bg=settings['background_color'])

    root.attributes("-topmost", settings['always_on_top'])
    root.configure(background=settings['background_color'])
    