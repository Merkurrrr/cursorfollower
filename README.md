# CursorFollower

A smooth, lagging cursor-following dot for Windows and Linux.
Lightweight, simple, and easy to customize.

---

## Features

* Smooth cursor following with configurable lag
* Cross-platform (Windows + Linux)
* Minimal and lightweight (no heavy dependencies)
* Easy to customize (size, color, smoothing)

---

## Installation

Make sure you have Python installed.

Tkinter is usually included with Python, but if not:

```bash
pip install tkinter
```

---

## Usage

Run the script:

```bash
python main.py
```

---

## Configuration

You can edit these values in the script:

* `DOT_SIZE` → size of the dot
* `LAG_SECONDS` → delay before the dot follows your cursor
* `SMOOTHING` → how smooth the movement is

Example:

```python
DOT_SIZE = 16
LAG_SECONDS = 0.2
SMOOTHING = 0.2
```

---

## Notes

* Works best on Windows and Linux (X11)
* On Wayland, global cursor tracking may be restricted
* Transparency behavior may vary depending on your system

---

## Use Cases

* Aesthetic cursor effects
* Screen recordings / demos
* Accessibility (easier cursor tracking)

---

## License

MIT License — feel free to use, modify, and distribute.

---

## Credits

Created by @cachyosguy

If you use or share this project, please give credit:

* TikTok: @cachyosguy
* Discord: @johngraingrace

---

## Have fun

Feel free to experiment, improve it, and share your versions.
