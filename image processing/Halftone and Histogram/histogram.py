
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter as tk

def calculate_histogram(image):
    if image.mode != 'L':
        image = image.convert('L') 

    histogram = [0] * 256
    bins = list(range(256))  
    image_array = np.array(image)
    for pixel in image_array.flatten():
        histogram[pixel] += 1

    return histogram, bins


def draw_text_on_image(image, text, x, y, font_size=9):
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    draw.text((x, y), text, fill="black", font=font)




def plot_histogram_tk(master, histogram):
    histogram_window = tk.Toplevel(master)
    histogram_window.title("Histogram")
    histogram_window.configure(bg="#f0f8ff")

    window_width = 1300
    window_height = 730
    screen_width = histogram_window.winfo_screenwidth()
    screen_height = histogram_window.winfo_screenheight()
    position_top = (screen_height // 2) - (window_height // 2)
    position_left = (screen_width // 2) - (window_width // 2)
    histogram_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    histogram_window.rowconfigure(0, weight=1)
    histogram_window.rowconfigure(1, weight=1)
    histogram_window.rowconfigure(2, weight=1)
    histogram_window.columnconfigure(0, weight=1)

    width, height = 800, 400
    margin = 30
    total_width, total_height = width + margin, height + margin
    hist_image = Image.new("RGB", (total_width, total_height), "white")
    max_value = max(histogram)

    draw = ImageDraw.Draw(hist_image)
    for i in range(256):
        bar_height = int((histogram[i] / max_value) * height)
        x0 = margin + i * 3
        y0 = height - bar_height
        x1 = x0 + 2
        y1 = height
        draw.rectangle([x0, y0, x1, y1], fill="gray")

    for i in range(0, 256, 25):
        x_pos = margin + i * 3
        draw_text_on_image(hist_image, str(i), x_pos, height + 5, font_size=10)

    y_tick_interval = max_value // 10 or 1
    for i in range(0, max_value + 1, y_tick_interval):
        y_pos = height - int((i / max_value) * height)
        draw_text_on_image(hist_image, str(i), 5, y_pos - 5, font_size=10)

    main_title = tk.Label(
        histogram_window,
        text="Histogram Result",
        font=("Arial", 20, "bold"),
        fg="#4a90e2",
        bg="#f0f8ff",
    )
    main_title.grid(row=0, column=0)

    tk_image = ImageTk.PhotoImage(hist_image)
    canvas = tk.Canvas(histogram_window, width=total_width, height=total_height, bg="white")
    canvas.grid(row=1, column=0)
    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.image = tk_image

    back_button = tk.Button(
        histogram_window,
        text="Back to Upload",
        command=histogram_window.destroy,
        bg="#4a90e2",
        fg="white",
        font=("Arial", 14),
    )
    back_button.grid(row=2, column=0)




