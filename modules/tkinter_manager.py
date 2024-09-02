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

    panel.bind("<B1-Motion>", lambda e: move(root, e))

    root.bind("<q>", lambda e: root.destroy())
    root.mainloop()

def move(root, e):
    x, y = root.winfo_pointerxy()
    root.geometry(f"+{x}+{y}")