from PIL import ImageGrab, Image
import sys
from modules import tkinter_manager
import os
import json

def main():
    # check sys args
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""

    if arg == "":
        img = ImageGrab.grabclipboard()

        if isinstance(img, Image.Image):
            wid, hgt = img.size
            tkinter_manager.make_window(wid, hgt, img)
        else:
            print("No image in clipboard.")

    elif "s" in arg or "--standard" in arg:
        # get image from clipboard
        img = ImageGrab.grabclipboard()

        if isinstance(img, Image.Image):
            # show img in standard program
            img.show()
        else:
            print("No image in clipboard.")

    elif arg == "--config":
        settings_file = os.path.expanduser("~") + "/.config/pinboard/settings.json"
        if os.path.isfile(settings_file):
            print(settings_file)
        else:
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
