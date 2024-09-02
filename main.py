from PIL import ImageGrab, Image
import sys
from modules import tkinter_manager

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

if __name__ == "__main__":
    main()
