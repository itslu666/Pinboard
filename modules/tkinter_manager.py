import tkinter as tk
from PIL import ImageTk, Image
from modules import settings_loader, image_handler
import sys
import platform

def make_window(open_windows, wid, hgt, img, win=None):
    win = win or tk.Tk()
    if win.winfo_name() == 'tk':
        win.withdraw()

    root = tk.Toplevel()
    open_windows[0] += 1
    # check if windows or linux
    if platform.system() == "Linux":
        root.wm_attributes('-type', 'splash')
    else:
        root.overrideredirect(True)
        
    root.attributes('-topmost', True)
    
    x, y = root.winfo_screenwidth() - wid - 30, 30
    root.geometry(f"{wid}x{hgt}+{x}+{y}")

    img_tk = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=wid, height=hgt, highlightbackground="black")
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    
    # Store references to avoid garbage collection
    root.img_tk = canvas.img_tk = img_tk
    canvas.img, canvas.img_x, canvas.img_y = img, 0, 0
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind events
    root.bind("<ButtonPress-1>", lambda e: get_start(e, root))
    root.bind("<B1-Motion>", lambda e: move(root, e))
    root.bind("<q>", lambda e: on_close_window(root, open_windows))
    root.bind("<KeyPress-plus>", lambda e: make_window(open_windows, *image_handler.get_image(), win))
    
    canvas.bind('<4>', lambda e: zoom_in(e, canvas, img, img.size))
    canvas.bind('<5>', lambda e: zoom_out(e, canvas, img, img.size))
    canvas.bind("<ButtonPress-2>", lambda e: start_move(e, canvas))
    canvas.bind("<B2-Motion>", lambda e: move_image(e, canvas))

    settings_loader.change_window(canvas)
    if win.winfo_name() == 'tk':
        win.mainloop()

def on_close_window(window, open_windows):
    window.destroy()
    open_windows[0] -= 1
    if open_windows[0] == 0:
        sys.exit()

def move(root, e):
    x = root.winfo_pointerx() - root.start_x
    y = root.winfo_pointery() - root.start_y
    root.geometry(f"+{x}+{y}")

def get_start(e, root):
    root.start_x, root.start_y = e.x_root - root.winfo_x(), e.y_root - root.winfo_y()

def zoom_in(e, canvas, img, og_size):
    current_width, current_height = canvas.img.size

    # Restrict resizing to 3 times the size
    if (current_width < 3 * og_size[0]) and (current_height < 3 * og_size[1]):
        canvas.img = img.resize((int(current_width * 1.2), int(current_height * 1.2)), Image.LANCZOS)
        canvas.img_x -= (e.x - canvas.canvasx(0)) * 0.2
        canvas.img_y -= (e.y - canvas.canvasy(0)) * 0.2

        canvas.img_tk = ImageTk.PhotoImage(canvas.img)
        canvas.delete("all")
        canvas.create_image(canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk)
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        print("Zoom limit reached")

def zoom_out(e, canvas, img, og_size):
    current_width, current_height = canvas.img.size

    if (current_width > og_size[0]) and (current_height > og_size[1]):
        new_width = max(int(current_width * 0.8), og_size[0])
        new_height = max(int(current_height * 0.8), og_size[1])

        canvas.img = img.resize((new_width, new_height), Image.LANCZOS)
        canvas.img_x += (e.x - canvas.canvasx(0)) * 0.2
        canvas.img_y += (e.y - canvas.canvasy(0)) * 0.2

        canvas.img_tk = ImageTk.PhotoImage(canvas.img)
        canvas.delete("all")
        canvas.create_image(canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk)
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        print("Original size reached")

def move_image(e, canvas):
    dx, dy = e.x - canvas.last_x, e.y - canvas.last_y
    canvas.img_x += dx
    canvas.img_y += dy

    canvas.delete("all")
    canvas.create_image(canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk)
    canvas.last_x, canvas.last_y = e.x, e.y

def start_move(e, canvas):
    canvas.last_x, canvas.last_y = e.x, e.y
