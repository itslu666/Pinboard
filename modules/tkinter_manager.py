import tkinter as tk
from PIL import ImageTk

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
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

    # binds
    root.bind("<ButtonPress-1>", lambda e: get_start(e, root))
    root.bind("<B1-Motion>", lambda e: move(root, e, root.start_x, root.start_y))
    root.bind("<q>", lambda e: root.destroy())

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

