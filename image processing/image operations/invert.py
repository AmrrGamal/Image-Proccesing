import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image


def invert(image):
    if image.mode != 'L':
        image = image.convert('L')

    img_array = np.array(image, dtype=np.float32)
    height, width = img_array.shape

    for i in range(height):
        for j in range(width):
            img_array[i, j] = 255 - img_array[i, j]

    img_array = np.clip(img_array, 0, 255)
    return Image.fromarray(img_array.astype(np.uint8))


def display_invert_result(master, original_image):
    if original_image:
        window = tk.Toplevel(master)
        window.title("Invert Result")
        window.configure(bg="#f0f8ff")

        window_width = 900
        window_height = 500
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        image = invert(original_image)

        if image:
            original_resized = original_image.resize((400, 300))
            resized = image.resize((400, 300))

            original_resized_photo = ImageTk.PhotoImage(original_resized)
            resized_image = ImageTk.PhotoImage(resized)

            main_title = tk.Label(window, text="Invert Result", font=("Arial", 18, "bold"), fg="#4a90e2", bg="#f0f8ff")
            main_title.grid(row=0, column=0,  columnspan=2, pady=(10, 0)) 

            original_label = tk.Label(window, image=original_resized_photo)
            original_label.image = original_resized_photo  
            original_label.grid(row=1, column=0, padx=20, pady=20)

            label = tk.Label(window, image=resized_image)
            label.image = resized_image  
            label.grid(row=1, column=1, padx=20, pady=20)

            original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            original_text.grid(row=2, column=0)

            text = tk.Label(window, text="Inverted Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            text.grid(row=2, column=1)

            back_button = tk.Button(window, text="Back to Upload", command=window.destroy, bg="#4a90e2", fg="white", font=("Arial", 14))
            back_button.grid(row=4, column=0, columnspan=2, pady=20)

    else:
        messagebox.showerror("Error", "Please upload an image first.")


