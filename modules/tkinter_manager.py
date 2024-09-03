import tkinter as tk
from PIL import ImageTk, Image

def make_window(wid, hgt, img):
    # make window
    root = tk.Tk()
    root.wm_attributes('-type', 'splash')
    root.attributes('-topmost', True)

    # get screen hight and width
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calc geometry if image and make window same size
    x = screen_width - wid - 30
    y = 30
    root.geometry(f"{wid}x{hgt}+{x}+{y}")

    # make image
    img_tk = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(root, width=wid, height=hgt)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.img = img
    canvas.img_tk = img_tk
    canvas.img_x = 0
    canvas.img_y = 0
    canvas.configure(scrollregion=canvas.bbox("all"))

    # binds
    root.bind("<ButtonPress-1>", lambda e: get_start(e, root))
    root.bind("<B1-Motion>", lambda e: move(root, e, root.start_x, root.start_y))
    root.bind("<q>", lambda e: root.destroy())

    canvas.bind('<4>', lambda e: zoom_in(e, canvas, img, img.size))
    canvas.bind('<5>', lambda e: zoom_out(e, canvas, img, img.size))

    # show window
    root.mainloop()

def move(root, e, start_x, start_y):
    # move window with pointer in same position
    x = root.winfo_pointerx() - start_x
    y = root.winfo_pointery() - start_y
    root.geometry(f"+{x}+{y}")

def get_start(e, root):
    # get and set pointer position
    start_x = e.x_root - root.winfo_x()
    start_y = e.y_root - root.winfo_y()

    root.start_x = start_x
    root.start_y = start_y

def zoom_in(e, canvas, img, og_size):
    current_width, current_height = canvas.img.size

    if (current_width < 3 * og_size[0]) and (current_height < 3 * og_size[1]):
        # update the global image reference
        canvas.img = img.resize((int(canvas.img.width * 1.2), int(canvas.img.height * 1.2)), Image.LANCZOS)

        # calc new pos to keep pointer centered
        canvas.img_x -= (e.x - canvas.canvasx(0)) * 0.2
        canvas.img_y -= (e.y - canvas.canvasy(0)) * 0.2

        # make photoimage
        img_tk = ImageTk.PhotoImage(canvas.img)
        # update the canvas with the new image
        canvas.delete("all")
        canvas.create_image(canvas.img_x, canvas.img_y, anchor=tk.NW, image=img_tk)

        # keep a reference to avoid garbage collection
        canvas.img_tk = img_tk
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        print("Zoom limit reached")

def zoom_out(e, canvas, img, og_size):
    current_width, current_height = canvas.img.size

    if (current_width > og_size[0]) and (current_height > og_size[1]):
        # update global image reference
        new_width = int(canvas.img.width * 0.8)
        new_height = int(canvas.img.height * 0.8)

        # the new size does not go below the original size
        new_width = max(new_width, og_size[0])
        new_height = max(new_height, og_size[1])

        canvas.img = img.resize((new_width, new_height), Image.LANCZOS)

        # calc new pos to keep pointer centered
        canvas.img_x += (e.x - canvas.canvasx(0)) * 0.2
        canvas.img_y += (e.y - canvas.canvasy(0)) * 0.2

        # make photoimage
        img_tk = ImageTk.PhotoImage(canvas.img)

        # update canvas
        canvas.delete("all")
        canvas.create_image(canvas.img_x, canvas.img_y, anchor=tk.NW, image=img_tk)

        # keep a reference to avoid garbage collection
        canvas.img_tk = img_tk
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        print("Original size reached")