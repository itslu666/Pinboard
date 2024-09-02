import tkinter as tk
from PIL import ImageTk

def make_window(wid, hgt, img):
    root = tk.Tk()
    root.wm_attributes('-type', 'splash')
    root.attributes('-topmost', True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - wid - 30
    y = 30
    root.geometry(f"{wid}x{hgt}+{x}+{y}")

    img_tk = ImageTk.PhotoImage(img)

    panel = tk.Label(root, image=img_tk)
    panel.pack(side="top", fill="both", expand="yes")
    panel.image = img_tk

    root.bind("<ButtonPress-1>", lambda e: get_start(e, root))
    root.bind("<B1-Motion>", lambda e: move(root, e, root.start_x, root.start_y))

    root.bind("<q>", lambda e: root.destroy())
    root.mainloop()

def move(root, e, start_x, start_y):
    x = root.winfo_pointerx() - start_x
    y = root.winfo_pointery() - start_y
    root.geometry(f"+{x}+{y}")

def get_start(e, root):
    start_x = e.x_root - root.winfo_x()
    start_y = e.y_root - root.winfo_y()

    root.start_x = start_x
    root.start_y = start_y

