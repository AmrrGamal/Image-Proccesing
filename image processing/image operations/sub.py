import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image

def subtract(image1, image2):
    if image1.mode != 'L':
        image1 = image1.convert('L')
    if image2.mode != 'L':
        image2 = image2.convert('L')

    if image1.size != image2.size:
        image2 = image2.resize(image1.size)    

    img_array1 = np.array(image1, dtype=np.float32)
    img_array2 = np.array(image2, dtype=np.float32)
    height, width = img_array1.shape

    subtracted_image = np.zeros((height, width), dtype=np.float32)

    for i in range(height):
        for j in range(width):
            subtracted_image[i, j] = img_array1[i, j] - img_array2[i, j]

    subtracted_image = np.clip(subtracted_image, 0, 255)
    return Image.fromarray(subtracted_image.astype(np.uint8))


def display_sub_result(master, original_image_1, original_image_2):
    window = tk.Toplevel(master)
    window.title("Subtracting Result")
    window.configure(bg="#f0f8ff")

    window_width = 1300
    window_height = 730

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = (screen_height // 2) - (window_height // 2)
    position_left = (screen_width // 2) - (window_width // 2)
    window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    subtracted_image = subtract(original_image_1, original_image_2)

    original_image_1_resized = ImageTk.PhotoImage(original_image_1.resize((300, 300)))
    original_image_2_resized = ImageTk.PhotoImage(original_image_2.resize((300, 300)))
    subtracted_image_resized = ImageTk.PhotoImage(subtracted_image.resize((300, 300)))

    main_title = tk.Label(window, text="Subtracting Result", font=("Arial", 20, "bold"), fg="#4a90e2", bg="#f0f8ff")
    main_title.grid(row=0, column=1,  columnspan=1, pady=(10, 0)) 

    original_image_1_label = tk.Label(window, image=original_image_1_resized)
    original_image_1_label.image = original_image_1_resized
    original_image_1_label.grid(row=1, column=0, padx=60, pady=10)

    original_image_2_label = tk.Label(window, image=original_image_2_resized)
    original_image_2_label.image = original_image_2_resized
    original_image_2_label.grid(row=1, column=1, padx=60, pady=10)

    subtracted_image_label = tk.Label(window, image=subtracted_image_resized)
    subtracted_image_label.image = subtracted_image_resized
    subtracted_image_label.grid(row=1, column=2, padx=60, pady=10)

    original_1_text = tk.Label(window, text="Original Image 1", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
    original_1_text.grid(row=2, column=0)

    original_2_text = tk.Label(window, text="Original Image 2", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
    original_2_text.grid(row=2, column=1)

    result_text = tk.Label(window, text="Subtracting result", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
    result_text.grid(row=2, column=2)

    back_button = tk.Button(window, text="Back to Upload", command=window.destroy, bg="#4a90e2", fg="white", font=("Arial", 14))
    back_button.grid(row=7, column=1, columnspan=1, pady=20)

