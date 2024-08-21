from PIL import ImageGrab, Image

# get image from clipboard
img = ImageGrab.grabclipboard()

if isinstance(img, Image.Image):
    # show img in standard program
    img.show()
else:
    print("No image in clipboard.")
