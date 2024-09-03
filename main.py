from PIL import ImageGrab, Image
import sys
from modules import tkinter_manager, image_handler
import os
import json

def main():
    settings_file = os.path.expanduser("~") + "/.config/pinboard/settings.json"
    if not os.path.isfile(settings_file):
        settings = {
                "border_color": "black",
                "background_color": "white"
            }

        with open(settings_file, 'w') as file:
            json.dump(settings, file, indent=4)

    # check sys args
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""

    if arg == "":
        open_windows = [0]
        tkinter_manager.make_window(open_windows)


    elif "s" in arg or "--standard" in arg:
        # get image from clipboard
        img = ImageGrab.grabclipboard()

        if isinstance(img, Image.Image):
            # show img in standard program
            img.show()
        else:
            print("No image in clipboard.")

    elif arg == "--create-config":
        settings = {
            "border_color": "black",
            "background_color": "white"
        }

        with open(settings_file, 'w') as file:
            json.dump(settings, file, indent=4)

    elif arg == "-h" or arg == "--help":
        with open("usage.txt", 'r') as file:
            print(file.read())

if __name__ == "__main__":
    main()
