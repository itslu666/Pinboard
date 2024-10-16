import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
from modules import settings_loader, image_handler
import sys
import platform


def make_window(open_windows, wid, hgt, img, win=None):
    win = win or tk.Tk()
    if win.winfo_name() == "tk":
        win.withdraw()

    root = tk.Toplevel()
    open_windows[0] += 1
    # check if windows or linux
    if platform.system() == "Linux":
        root.wm_attributes("-type", "splash")

    root.attributes("-topmost", True)

    x, y = root.winfo_screenwidth() - wid - 30, 30
    root.geometry(f"{wid}x{hgt}+{x}+{y}")

    root.initial_width = wid
    root.initial_height = hgt

    img_tk = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=wid, height=hgt, highlightbackground="black")
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

    # Store references to avoid garbage collection
    root.img_tk = canvas.img_tk = img_tk
    canvas.img, canvas.img_x, canvas.img_y = img, 0, 0
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind events
    # moving
    root.bind("<ButtonPress-1>", lambda e: get_start(e, root))
    root.bind("<B1-Motion>", lambda e: move(root, e))

    # close/open
    settings = settings_loader.load_settings()
    root.bind(
        f"<{settings['close_key']}>", lambda e: on_close_window(root, open_windows)
    )
    root.bind(
        f"<{settings['open_key']}>",
        lambda e: make_window(open_windows, *image_handler.get_image(), win),
    )

    # zoom/panning
    canvas.bind("<4>", lambda e: zoom_in(e, canvas, img, img.size))
    canvas.bind("<5>", lambda e: zoom_out(e, canvas, img, img.size))
    canvas.bind("<ButtonPress-2>", lambda e: start_move(e, canvas))
    canvas.bind("<B2-Motion>", lambda e: move_image(e, canvas))

    # resizing
    root.bind("<ButtonPress-3>", lambda e: start_resize(e, root))
    root.bind("<B3-Motion>", lambda e: perform_resize(e, root, canvas, img, False))
    root.bind(
        f"<{settings['reset_size_key']}>",
        lambda e: reset_size(e, root, canvas, img, img.size),
    )
    root.bind("<KeyPress-comma>", lambda e: perform_resize(e, root, canvas, img, ","))
    root.bind("<KeyPress-period>", lambda e: perform_resize(e, root, canvas, img, "."))

    # rotating
    root.bind("<r>", lambda e: rotate(e, canvas, root))

    # load settings
    settings_loader.change_window(canvas, root)

    # make buttons if enabled
    if settings["buttons"]:
        add_button = ctk.CTkButton(
            canvas,
            text=" ",
            font=("", 20),
            width=50,
            command=lambda: root.event_generate(f"<{settings['open_key']}>"),
        )
        close_button = ctk.CTkButton(
            canvas,
            text=" ",
            font=("", 20),
            width=50,
            command=lambda: root.event_generate(f"<{settings['close_key']}>"),
        )
        increase_size_button = ctk.CTkButton(
            canvas,
            text="+",
            font=("", 20),
            width=50,
            command=lambda: root.event_generate("<KeyPress-period>"),
        )
        decrease_size_button = ctk.CTkButton(
            canvas,
            text="-",
            font=("", 20),
            width=50,
            command=lambda: root.event_generate("<KeyPress-comma>"),
        )
        reset_size_button = ctk.CTkButton(
            canvas,
            text=" ",
            font=("", 20),
            width=50,
            command=lambda: root.event_generate(f"{settings['reset_size_key']}"),
        )
        rotate_left_button = ctk.CTkButton(
            canvas,
            text=" ",
            font=("", 20),
            width=50,
            command=lambda: root.event_generate("<KeyPress-r>"),
        )
        rotate_right_button = ...

        add_button.pack(anchor="ne", pady=(0, 5))
        close_button.pack(anchor="ne", pady=5)
        increase_size_button.pack(anchor="ne", pady=5)
        decrease_size_button.pack(anchor="ne", pady=5)
        reset_size_button.pack(anchor="ne", pady=5)
        rotate_left_button.pack(anchor="ne", pady=(5, 0))

    if win.winfo_name() == "tk":
        win.mainloop()


def start_resize(e, root):
    root.start_x, root.start_y = e.x_root, e.y_root
    root.start_width, root.start_height = root.winfo_width(), root.winfo_height()


def perform_resize(e, root, canvas, img, pressed_key):
    if pressed_key:
        root.start_width, root.start_height = root.winfo_width(), root.winfo_height()
        if pressed_key == ",":
            new_width = int(root.start_width * 0.8)
            new_height = int(root.start_height * 0.8)
        elif pressed_key == ".":
            new_width = int(root.start_width * 1.2)
            new_height = int(root.start_height * 1.2)
    else:
        new_width = root.start_width + (e.x_root - root.start_x)
        new_height = root.start_height + (e.y_root - root.start_y)

    if new_width > 100 and new_height > 100:
        root.geometry(f"{new_width}x{new_height}")
        canvas.config(width=new_width, height=new_height)

        # image resizing
        canvas.img = img.resize((int(new_width), int(new_height)), Image.LANCZOS)
        canvas.img_tk = ImageTk.PhotoImage(canvas.img)
        canvas.delete("all")
        canvas.create_image(
            canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk
        )


def reset_size(e, root, canvas, img, og_size):
    canvas.img = img.resize((og_size[0], og_size[1]), Image.LANCZOS)

    canvas.img_tk = ImageTk.PhotoImage(canvas.img)
    canvas.delete("all")
    canvas.create_image(canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk)
    root.geometry(f"{root.initial_width}x{root.initial_height}")


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
        canvas.img = img.resize(
            (int(current_width * 1.2), int(current_height * 1.2)), Image.LANCZOS
        )
        canvas.img_x -= (e.x - canvas.canvasx(0)) * 0.2
        canvas.img_y -= (e.y - canvas.canvasy(0)) * 0.2

        canvas.img_tk = ImageTk.PhotoImage(canvas.img)
        canvas.delete("all")
        canvas.create_image(
            canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk
        )
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
        canvas.create_image(
            canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk
        )
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


def rotate(e, canvas, root):
    canvas.img = canvas.img.rotate(90, expand=True)
    canvas.img_tk = ImageTk.PhotoImage(canvas.img)
    canvas.create_image(canvas.img_x, canvas.img_y, anchor=tk.NW, image=canvas.img_tk)

    # set new dimensions
    width = root.winfo_width()
    height = root.winfo_height()
    root.geometry(f"{height}x{width}")
