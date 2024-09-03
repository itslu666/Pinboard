from PIL import ImageGrab, Image
import sys

def get_image():
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        return img.size[0], img.size[1], img
    else:
        print("No image in clipboard")
        sys.exit()