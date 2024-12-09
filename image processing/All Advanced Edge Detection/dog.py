import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image
import cv2

mask_7x7 = np.array([
    [0, 0, -1, -1, -1, 0, 0],
    [0, -2, -3, -3, -3, -2, 0],
    [-1, -3, 5, 5, 5, -3, -1],
    [-1, -3, 5, 16, 5, -3, -1],
    [-1, -3, 5, 5, 5, -3, -1],
    [0, -2, -3, -3, -3, -2, 0],
    [0, 0, -1, -1, -1, 0, 0]
], dtype=np.float32)
mask_9x9 = np.array([
    [0, 0, 0, -1, -1, -1, 0, 0, 0],
    [0, -2, -3, -3, -3, -3, -3, -2, 0],
    [0, -3, -2, -1, -1, -1, -2, -3, 0],
    [-1, -3, -1, 9, 9, 9, -1, -3, -1],
    [-1, -3, -1, 9, 19, 9, -1, -3, -1],
    [-1, -3, -1, 9, 9, 9, -1, -3, -1],
    [0, -3, -2, -1, -1, -1, -2, -3, 0],
    [0, -2, -3, -3, -3, -3, -3, -2, 0],
    [0, 0, 0, -1, -1, -1, 0, 0, 0]
], dtype=np.float32)

def difference_of_gaussians(image):
    if image.mode != 'L':
        image = image.convert('L')
    
    img_array = np.array(image, dtype=np.float32)
    image_7x7 = cv2.filter2D(img_array, -1, mask_7x7)
    image_9x9 = cv2.filter2D(img_array, -1, mask_9x9)

    dog = image_7x7 - image_9x9

    dog = np.clip(dog, 0, 255).astype(np.uint8)
    image_7x7 = np.clip(image_7x7, 0, 255).astype(np.uint8)
    image_9x9 = np.clip(image_9x9, 0, 255).astype(np.uint8)

    return Image.fromarray(dog),Image.fromarray(image_7x7) ,Image.fromarray(image_9x9)


def display_dog_result(master, original_image):
   if original_image:
        window = tk.Toplevel(master)
        window.title("Difference of Gaussians Result")
        window.configure(bg="#f0f8ff")
        
        window_width = 1300
        window_height = 730
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        dog,image_7x7 ,image_9x9 = difference_of_gaussians(original_image)

        original_resized = ImageTk.PhotoImage(original_image.resize((300, 240)))
        dog_resized = ImageTk.PhotoImage(dog.resize((300, 240)))
        image_7x7_resized = ImageTk.PhotoImage(image_7x7.resize((300, 240)))
        image_9x9_resized = ImageTk.PhotoImage(image_9x9.resize((300, 240)))

        main_title = tk.Label(window, text="Difference of Gaussians Result", font=("Arial", 20, "bold"), fg="#4a90e2", bg="#f0f8ff")
        main_title.grid(row=0, column=1,  columnspan=1, pady=(10, 0))

        original_label = tk.Label(window, image=original_resized)
        original_label.image = original_resized
        original_label.grid(row=1, column=0, padx=70, pady=10)

        dog_label = tk.Label(window, image=dog_resized)
        dog_label.image = dog_resized
        dog_label.grid(row=1, column=1,  padx=40 ,pady=10)

        image_7x7_label = tk.Label(window, image=image_7x7_resized)
        image_7x7_label.image = image_7x7_resized
        image_7x7_label.grid(row=1, column=2,padx=40, pady=10)

        image_9x9_label = tk.Label(window, image=image_9x9_resized)
        image_9x9_label.image = image_9x9_resized
        image_9x9_label.grid(row=3, column=1, padx=40, pady=10)

        original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        original_text.grid(row=2, column=0)

        dog_text = tk.Label(window, text="DOG Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        dog_text.grid(row=2, column=1)

        image_7x7_text = tk.Label(window, text="7X7_Mask Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        image_7x7_text.grid(row=2, column=2)

        image_9x9_text = tk.Label(window, text="9X9_Mask Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        image_9x9_text.grid(row=4, column=1)

   else:
        messagebox.showerror("Error", "Please upload an image first.")
