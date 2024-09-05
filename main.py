from PIL import ImageGrab, Image
import sys
from modules import tkinter_manager, image_handler
import os
import json
from tkinter import filedialog

def main():
    # setting file checks
    settings_file = os.path.expanduser("~") + "/.config/pinboard/settings.json"
    if not os.path.isfile(settings_file):
        settings = {
                "border_color": "black",
                "background_color": "white"
            }
        with open(settings_file, 'w') as file:
            json.dump(settings, file, indent=4)

    if "-f" in sys.argv or "--file" in sys.argv:
        path = filedialog.askopenfilename(
            title="Choose an image",
            filetypes=[("Images", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )
        if path:
            img = Image.open(path)
            
            if "-s" in sys.argv:
                img.show()

            if "-p" in sys.argv:
                tkinter_manager.make_window([0], img.size[0], img.size[1], img)


    # handle args
    if ("-s" in sys.argv or "--standard" in sys.argv) and ("-f" not in sys.argv and "--file" not in sys.argv):
        # get img and show in default app
        _, _, img = image_handler.get_image()
        img.show()

    if len(sys.argv) == 1 or "-p" in sys.argv or "--pin" in sys.argv:
        open_windows = [0]
        wid, hgt, img = image_handler.get_image()
        tkinter_manager.make_window(open_windows, wid, hgt, img)



    # OTHER
    if "--create-config" in sys.argv:
        settings = {
            "border_color": "black",
            "background_color": "white"
        }

        with open(settings_file, 'w') as file:
            json.dump(settings, file, indent=4)

    if "-h" in sys.argv or "--help" in sys.argv:
        with open("usage.txt", 'r') as file:
            print(file.read())

if __name__ == "__main__":
    main()
