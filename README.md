# Pinboard
Pinboard is a simple Python Tkinter app that can pin your images to your desktop.

### Features
- Pin images to desktop
- Pin from clipboard to desktop
- Open image in image viewer from clipboard
- Change border / background color
- Drag images across your screen
- Zoom into images
- Pan images inside the window
- Resize images
- Show/hide shortcut buttons

### TODO:
- [ ] Add rotation
- [ ] Fix zooming on windows

---
### Installation
You need to install the `tkinter` system package **and** `xclip` for X11 or `wl-clipboard` for Wayland before building:\
To see what XDG session you are running: `echo $XDG_SESSION_TYPE`

#### X11:
Ubuntu/Debian: 

    sudo apt-get install python3-tk xclip

Fedora:

    sudo dnf install python3-tkinter xclip

Arch: 
    
    sudo pacman -S tk xclip

#### Wayland:
Ubuntu/Debian: 

    sudo apt-get install python3-tk wl-clipboard

Fedora: 

    sudo dnf install python3-tkinter wl-clipboard

Arch:

    sudo pacman -S tk wl-clipboard

#### Building:
    git clone https://github.com/itslu666/Pinboard.git
    cd Pinboard
    make
\
The executable will be in `dist` you can use it in there or move it to somewhere in your PATH. e.g.:
        
    sudo mv dist/pinboard /usr/bin/
\
Optional cleaning (removes `dist` too):

    make clean

---
### Uninstalling
    make uninstall
(Don't forget to remove the executable in /usr/bin/pinboard if you moved it)

---
### Usage:
    pinboard [option]
Option |   Effect
--  |   --
-h, --help  |   Display help
-s, --standard  | Open clipboard image in default image viewer
-p, --pin   |   Pin image to desktop (like if you don't pass arg)
-f, --file  |   Select a file to display (need to specify -p or -s)
--create-config |   Make config file (Warning: Overwrites current file if existing)

For peak experience make a keyboard shortcut to execute `pinboard`

Drag the image on your display\
Pan the image with `mouswheel click`\
Zoom the image with `scroll`\
Resize the image with `right click and drag`

Press `+` to add another image from clipboard\
Press `q` to close the selected image\
Press `,` to proportionally decrease image size\
Press `.` to proportionally increase image size\
Press `b` to reset the image size

---
### Settings:
Option  |   Value   |   Effect  |   Example |   Default
--  |   --  |   --  |   --  |   ---
border_color    |   any color   |   Changes the color of the pin border |   red/#ff0000 |   black
background_color    |   any color   |   Changes the background color when image panned out of bounds    |   red/#ff0000 |   white
always_on_top   |   True/False  |   Wether the pin should be always on top or not   |   true    |   true
close_key   |   any key symbol    |   Defines the closing key |   w   |   q
open_key    |   any key symbol    |   Defines the opening key |   p   | KeyPress-plus
reset_size_key  |   any key symbol  |   Defines the reset size key  |   Control-z   |   b
buttons |   True/False  |   Shows shortcut buttons  |   true    |   false

Settings file is in `~/.config/pinboard/settings.json` after first execution\
For the keybinds, you can find a list of keysyms here: http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

---
Tested on:\
Windows\
Arch Linux X11/Wayland