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
    canvas.configure(scrollregion=canvas.bbox("all"))

    # binds
    root.bind("<ButtonPress-1>", lambda e: get_start(e, root))
    root.bind("<B1-Motion>", lambda e: move(root, e, root.start_x, root.start_y))
    root.bind("<q>", lambda e: root.destroy())

    canvas.bind('<4>', lambda e: zoom_in(e, canvas, img))
    canvas.bind('<5>', lambda e: zoom_out(e, canvas, img))

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

def zoom_in(e, canvas, img):
    # Update the global image reference
    canvas.img = img.resize((int(canvas.img.width * 1.2), int(canvas.img.height * 1.2)), Image.LANCZOS)
    # Convert updated image to PhotoImage
    img_tk = ImageTk.PhotoImage(canvas.img)
    # Update the canvas with the new image
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    # Keep a reference to avoid garbage collection
    canvas.img_tk = img_tk
    canvas.configure(scrollregion=canvas.bbox("all"))



def zoom_out(e, canvas, img):
    # Update the global image reference
    canvas.img = img.resize((int(canvas.img.width * 0.9), int(canvas.img.height * 0.9)), Image.LANCZOS)
    # Convert updated image to PhotoImage
    img_tk = ImageTk.PhotoImage(canvas.img)
    # Update the canvas with the new image
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    # Keep a reference to avoid garbage collection
    canvas.img_tk = img_tk
    canvas.configure(scrollregion=canvas.bbox("all"))