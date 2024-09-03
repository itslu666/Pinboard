# Pinboard
Pinboard is a simple Python Tkinter app that can pin your images on your desktop.

### Features
- Pin images to desktop (duh)
- Pin screenshots to desktop
- Change border / background color
- Drag images across your screen
- Zoom into images
- Move images inside the window
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
`make clean`\
\
The executable will be in `dist` you can use it in there or move it to somewhere in your path. e.g.:\
`sudo mv dist/pinboard /usr/bin/`

#### Manual:
`git clone https://github.com/itslu666/Pinboard.git`\
`mkdir ~/.config/pinboard`\
`python main.py --config`\
`python main.py [option]`

---
### Uninstalling
`make uninstall`

---
### Usage:
`pinboard [option]`\
Tag |   Effect
--  |   --
