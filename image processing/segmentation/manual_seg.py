import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox 

def manual_segmentation(image, low_threshold, high_threshold):
    if image.mode != 'L': 
        image = image.convert('L')
    
    img_array = np.array(image, dtype=np.float32)
    segmented_image = np.zeros_like(img_array)
    segmented_image[(img_array >= low_threshold) & (img_array <= high_threshold)] = 255
    segmented_image = np.clip(segmented_image, 0, 255)

    return Image.fromarray(segmented_image.astype(np.uint8)) 

def display_manual_segmentation_result(master, original_image, low_threshold, high_threshold):
    if original_image:
    
        window = tk.Toplevel(master)
        window.title("Manual Segmentation Result")
        window.configure(bg="#f0f8ff")

        window_width = 900
        window_height = 500
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
    
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        
        manual_segmented = manual_segmentation(original_image, low_threshold, high_threshold)

        if manual_segmented:
            original_resized = ImageTk.PhotoImage(original_image.resize((400, 300)))
            manual_segmented_resized = ImageTk.PhotoImage(manual_segmented.resize((400, 300)))

            main_title = tk.Label(window, text="Manual Segmentation Result", font=("Arial", 18, "bold"), fg="#4a90e2", bg="#f0f8ff")
            main_title.grid(row=0, column=0,  columnspan=2, pady=(10, 0))

            original_label = tk.Label(window, image=original_resized)
            original_label.image = original_resized
            original_label.grid(row=1, column=0, padx=20, pady=20)

            manual_segmented_label = tk.Label(window, image=manual_segmented_resized)
            manual_segmented_label.image = manual_segmented_resized
            manual_segmented_label.grid(row=1, column=1, padx=20, pady=20)

            original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            original_text.grid(row=2, column=0)

            halftoned_text = tk.Label(window, text="Manual Segmentation Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            halftoned_text.grid(row=2, column=1)

            back_button = tk.Button(window, text="Back to Upload", command=window.destroy, bg="#4a90e2", fg="white", font=("Arial", 14))
            back_button.grid(row=3, column=0, columnspan=2, pady=20)

        
