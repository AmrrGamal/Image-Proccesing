import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image
     

def advanced_halftoning_using_error_diffusion(image, threshold=128):
    if image.mode != 'L':
        image = image.convert('L')
        
    img_array = np.array(image, dtype=np.float32)
    height, width = img_array.shape

    for i in range(height):
        for j in range(width):
            old_pixel = img_array[i, j]
            new_pixel = 255 if old_pixel >= threshold else 0
            img_array[i, j] = new_pixel
            error = old_pixel - new_pixel
            if j + 1 < width:
                img_array[i, j + 1] += error * 7 / 16
            if i + 1 < height and j > 0:
                img_array[i + 1, j - 1] += error * 3 / 16
            if i + 1 < height:
                img_array[i + 1, j] += error * 5 / 16
            if i + 1 < height and j + 1 < width:
                img_array[i + 1, j + 1] += error * 1 / 16

    img_array = np.clip(img_array, 0, 255)
    return Image.fromarray(img_array.astype(np.uint8))

def display_advanced_halftoning_result(master, original_image):
    if original_image:
        halftoning_window = tk.Toplevel(master)
        halftoning_window.title("Halftoning Result")
        halftoning_window.configure(bg="#f0f8ff")

        window_width = 900
        window_height = 500

        screen_width = halftoning_window.winfo_screenwidth()
        screen_height = halftoning_window.winfo_screenheight()
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        halftoning_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        advanced_halftoned_image = advanced_halftoning_using_error_diffusion(original_image)

        if advanced_halftoned_image :
           
            main_title = tk.Label(halftoning_window, text="Advanced Halftoning Result", font=("Arial", 18, "bold"), fg="#4a90e2", bg="#f0f8ff")
            main_title.grid(row=0, column=0,  columnspan=2, pady=(10, 0))  
        
            original_resized = ImageTk.PhotoImage(original_image.resize((400, 300)))
            halftoned_resized = ImageTk.PhotoImage(advanced_halftoned_image.resize((400, 300)))

            original_label = tk.Label(halftoning_window, image=original_resized)
            original_label.image = original_resized
            original_label.grid(row=1, column=0, padx=20, pady=20)

            halftoned_label = tk.Label(halftoning_window, image=halftoned_resized)
            halftoned_label.image = halftoned_resized
            halftoned_label.grid(row=1, column=1, padx=20, pady=20)

            original_text = tk.Label(halftoning_window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            original_text.grid(row=2, column=0)

            halftoned_text = tk.Label(halftoning_window, text="Advanced Halftoned Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            halftoned_text.grid(row=2, column=1)

            back_button = tk.Button(halftoning_window, text="Back to Upload", command=halftoning_window.destroy, bg="#4a90e2", fg="white", font=("Arial", 14))
            back_button.grid(row=4, column=0, columnspan=2, pady=20)

    else:
        messagebox.showerror("Error", "Please upload an image first.")

