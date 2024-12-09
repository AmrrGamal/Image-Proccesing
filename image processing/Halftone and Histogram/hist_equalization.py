import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image
from histogram import calculate_histogram 
import numpy as np
from PIL import Image 

def histogram_equalization(image):
    if image.mode != 'L':
        image = image.convert('L') 

    histogram, bins = calculate_histogram(image)

    cdf = np.cumsum(histogram)
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min()) 

    img_array = np.array(image)
    flat = img_array.flatten()

    equalized_flat = np.interp(flat, bins, cdf_normalized).astype(np.uint8)
    equalized_img_array = equalized_flat.reshape(img_array.shape)
    equalized_image = Image.fromarray(equalized_img_array)
    equalized_histogram, _ = calculate_histogram(equalized_image)

    return equalized_image, equalized_histogram


def draw_text_on_image(image, text, x, y, font_size=9):
 
    from PIL import ImageDraw, ImageFont

    draw = ImageDraw.Draw(image)
    try:
        
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default() 
    draw.text((x, y), text, fill="black", font=font)



def plot_histogram(histogram, width, height):

    margin = 50  
    hist_image = Image.new("RGB", (width + margin, height + margin), "white")
    pixels = hist_image.load()

    max_hist = max(histogram)

    for x in range(256):
        bar_height = int((histogram[x] / max_hist) * height)
        for y in range(height - bar_height, height):
            pixels[x + margin, y] = (0, 0, 0)  

    for x in range(0, 256, 25): 
        x_pos = int((x / 255) * width) + margin
        for y in range(height, height + 5):
            pixels[x_pos, y] = (0, 0, 0)
        
        draw_text_on_image(hist_image, str(x), x_pos - 10, height + 10, font_size=9)

    step = max_hist // 10 or 1  
    for y in range(0, max_hist + step, step):
        y_pos = height - int((y / max_hist) * height)
        for x in range(margin - 5, margin):  
            pixels[x, y_pos] = (0, 0, 0)
       
        draw_text_on_image(hist_image, str(y), 5, y_pos - 8, font_size=9)

    for x in range(margin - 5, width + margin):
        pixels[x, height] = (0, 0, 0)  
    for y in range(0, height + 1):
        pixels[margin, y] = (0, 0, 0) 

    return hist_image


def display_hist_eq_result(master, original_image):
    if original_image:
        window = tk.Toplevel(master)
        master = master
        window.title("Histogram Equalization Result")
        window.configure(bg="#f0f8ff")

        window_width = 1300
        window_height = 730
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        image, hist = histogram_equalization(original_image)

        main_title = tk.Label(window, text="Histogram Equalization Result", font=("Arial", 20, "bold"), fg="#4a90e2", bg="#f0f8ff")
        main_title.grid(row=0, column=1,  pady=(10, 0)) 

        original_resized = ImageTk.PhotoImage(original_image.resize((300, 300)))
        equalized_resized = ImageTk.PhotoImage(image.resize((300, 300)))

        hist_image = plot_histogram(hist, width=275, height=150)
        hist_resized = ImageTk.PhotoImage(hist_image.resize((300, 300)))

        original_label = tk.Label(window, image=original_resized)
        original_label.image = original_resized
        original_label.grid(row=1, column=0, padx=60, pady=10)

        equalized_label = tk.Label(window, image=equalized_resized)
        equalized_label.image = equalized_resized
        equalized_label.grid(row=1, column=1, padx=60, pady=10)

        hist_label = tk.Label(window, image=hist_resized)
        hist_label.image = hist_resized
        hist_label.grid(row=1, column=2, padx=60, pady=10)

        original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        original_text.grid(row=2, column=0)

        equalized_text = tk.Label(window, text="Equalized Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        equalized_text.grid(row=2, column=1)

        hist_text = tk.Label(window, text="Histogram of the Equalized Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        hist_text.grid(row=2, column=2)

        back_button = tk.Button(window, text="Back to Upload", command=window.destroy, bg="#4a90e2", fg="white", font=("Arial", 14))
        back_button.grid(row=4, column=1 ,pady=20)


    else:
        messagebox.showerror("Error", "Please upload an image first.")