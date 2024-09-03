# Pinboard
Pinboard is a simple Python Tkinter app that can pin your images on your desktop.

### Features
- Pin images to desktop (duh)
- Pin screenshots to desktop
- Change border / background color
- Drag images across your screen
- Zoom into images
- Move images inside the window

### TODO:
- [ ] Add file import
- [ ] Add resize window feature
- [ ] Fix canvas bounds


---
### Installation
You need to install the `tkinter` system package **and** `xclip` for X11 or `wl-clipboard` for Wayland before building:\
To see what XDG session you are running: `echo $XDG_SESSION_TYPE`

X11:\
Arch: `sudo pacman -S tk xclip`

Wayland:\
Arch: `sudo pacman -S tk wl-clipboard`
#### Building:
`git clone https://github.com/itslu666/Pinboard.git`\
`cd Pinboard`\
`make`\
\
The executable will be in `dist` you can use it in there or move it to somewhere in your path. e.g.:\
`sudo mv dist/pinboard /usr/bin/`\
\
Optional cleaning (removes `dist` too):\
`make clean`

#### Manual:
`git clone https://github.com/itslu666/Pinboard.git`\
`mkdir ~/.config/pinboard`\
`python main.py --config`\
`python main.py [option]`

---
### Uninstalling
`make uninstall`\
(don't forget to remove the executable in /usr/bin/pinboard if you moved it)

---
### Usage:
`pinboard [option]`
Tag |   Effect
--  |   --
-h, --help  |   Display help
-s, --standard  | Open clipboard image in default image viewer
--create-config |   Make config file (Warning: Overwrites current file if existing)

For peak experience make a keyboard shortcut to execute `pinboard`