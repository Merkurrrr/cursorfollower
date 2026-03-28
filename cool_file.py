import tkinter as tk
import time

# --- Settings ---
DOT_SIZE = 16
LAG_SECONDS = 0.2
SMOOTHING = 0.2  # 0 < smoothing < 1

# --- State ---
positions = []
current_x, current_y = 0, 0

# --- Setup window ---
root = tk.Tk()
root.overrideredirect(True)  # no border
root.attributes("-topmost", True)

# Transparent background (works differently per OS)
try:
    root.attributes("-transparentcolor", "black")
    bg_color = "black"
except:
    bg_color = root["bg"]

canvas = tk.Canvas(root, width=DOT_SIZE, height=DOT_SIZE,
                   highlightthickness=0, bg=bg_color)
canvas.pack()

# Draw white dot
canvas.create_oval(2, 2, DOT_SIZE-2, DOT_SIZE-2, fill="gray", outline="white")

# --- Update loop ---
def update():
    global current_x, current_y

    now = time.time()

    # Get mouse position
    mouse_x = root.winfo_pointerx()
    mouse_y = root.winfo_pointery()

    positions.append((now, (mouse_x, mouse_y)))

    # Keep only recent positions
    positions[:] = [(t, pos) for t, pos in positions if now - t <= LAG_SECONDS + 0.1]

    # Find lagged target
    target_x, target_y = mouse_x, mouse_y
    for t, pos in positions:
        if now - t >= LAG_SECONDS:
            target_x, target_y = pos
            break

    # Smooth movement (lerp)
    current_x += (target_x - current_x) * SMOOTHING
    current_y += (target_y - current_y) * SMOOTHING

    # Move window
    root.geometry(f"{DOT_SIZE}x{DOT_SIZE}+{int(current_x)}+{int(current_y)}")

    root.after(10, update)

# Start loop
update()
root.mainloop()