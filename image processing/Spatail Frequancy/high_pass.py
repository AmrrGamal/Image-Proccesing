import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox 
from PIL import Image
import numpy as np
import cv2

def high_pass_filter(image):
    if image.mode != 'L':
        image = image.convert('L')

    img_array = np.array(image, dtype=np.float32)
    
    mask_3x3_high_pass = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float32)
    
    filtered_array = cv2.filter2D(img_array, -1, mask_3x3_high_pass)
    filtered_array = np.clip(filtered_array, 0, 255)
    return Image.fromarray(filtered_array.astype(np.uint8))

def display_high_pass_filter_result(master, original_image):
   if original_image:
        window = tk.Toplevel(master)
        window.title("High Pass Filter Result")
        window.configure(bg="#f0f8ff")
        
        window_width = 900
        window_height = 500
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        image = high_pass_filter(original_image)

        if image:
            original_resized = ImageTk.PhotoImage(original_image.resize((400, 300)))
            resized = ImageTk.PhotoImage(image.resize((400, 300)))

            main_title = tk.Label(window, text="High Pass Filter Result", font=("Arial", 18, "bold"), fg="#4a90e2", bg="#f0f8ff")
            main_title.grid(row=0, column=0,  columnspan=2, pady=(10, 0))

            original_label = tk.Label(window, image=original_resized)
            original_label.image = original_resized
            original_label.grid(row=1, column=0, padx=20, pady=20)

            label = tk.Label(window, image=resized)
            label.image = resized
            label.grid(row=1, column=1, padx=20, pady=20)

            original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            original_text.grid(row=2, column=0)

            text = tk.Label(window, text="High Pass Filter Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            text.grid(row=2, column=1)

            back_button = tk.Button(window, text="Back to Upload", command=window.destroy, bg="#4a90e2", fg="white", font=("Arial", 14))
            back_button.grid(row=3, column=0, columnspan=2, pady=20)

        else:
          messagebox.showerror("Error", "Please upload an image first.")