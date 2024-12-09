import tkinter as tk 
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image
from homogeneity import homogeneity_operator
from difference import difference_operator
from variance import variance_operator
from contrast_based import contrast_based_edge_detection
from dog import difference_of_gaussians
from range import range_operator


def all_advanced_operator(image):
    
    range_image = range_operator(image)
    dog_image,image_7x7,image_9x9 = difference_of_gaussians(image)
    diff_image = difference_operator(image)
    var_image = variance_operator(image)
    home_image = homogeneity_operator(image)
    contrast_image = contrast_based_edge_detection(image)

    return range_image ,dog_image,diff_image,var_image,home_image,contrast_image,image_9x9
   

def display_all_advanced_result(master, original_image):
   if original_image:
        window = tk.Toplevel(master)
        window.title("All Advanced Edge Detection Techniques Result")
        window.geometry("1200x600")
        window.configure(bg="#f0f8ff")
        
        window_width = 1300
        window_height = 730
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        range_image ,dog_image,diff_image,var_image,home_image,contrast_image,image_9x9 = all_advanced_operator(original_image)

        original_resized = ImageTk.PhotoImage(original_image.resize((250, 250)))
        range_image = ImageTk.PhotoImage(range_image.resize((250, 250)))
        dog_image = ImageTk.PhotoImage(dog_image.resize((250, 250)))
        diff_image = ImageTk.PhotoImage(diff_image.resize((250, 250)))
        var_image = ImageTk.PhotoImage(var_image.resize((250, 250)))
        home_image = ImageTk.PhotoImage(home_image.resize((250, 250)))
        contrast_image = ImageTk.PhotoImage(contrast_image.resize((250, 250)))
        image_9x9 = ImageTk.PhotoImage(image_9x9.resize((250, 250)))
        

        original_label = tk.Label(window, image=original_resized)
        original_label.image = original_resized
        original_label.grid(row=0, column=0, padx=30, pady=10)

        range_label = tk.Label(window, image=range_image)
        range_label.image = range_image
        range_label.grid(row=0, column=1, padx=30, pady=10)

        dog_label = tk.Label(window, image=dog_image)
        dog_label.image = dog_image
        dog_label.grid(row=0, column=2, padx=30, pady=10)

        diff_label = tk.Label(window, image=diff_image)
        diff_label.image = diff_image
        diff_label.grid(row=0, column=3, padx=30, pady=10)

        var_label = tk.Label(window, image=var_image)
        var_label.image = var_image
        var_label.grid(row=2, column=0, padx=30, pady=10)

        hame_label = tk.Label(window, image=home_image)
        hame_label.image = home_image
        hame_label.grid(row=2, column=1, padx=30, pady=10)

        contrast_label = tk.Label(window, image=contrast_image)
        contrast_label.image = contrast_image
        contrast_label.grid(row=2, column=2, padx=30, pady=10)

        image_9x9_label = tk.Label(window, image=image_9x9)
        image_9x9_label.image = image_9x9
        image_9x9_label.grid(row=2, column=3, padx=30, pady=10)

        original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        original_text.grid(row=1, column=0)

        range_text = tk.Label(window, text="Range Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        range_text.grid(row=1, column=1)

        dog_text = tk.Label(window, text="DOG Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        dog_text.grid(row=1, column=2)

        diff_text = tk.Label(window, text="Difference Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        diff_text.grid(row=1, column=3)

        var_text = tk.Label(window, text="Variance Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        var_text.grid(row=3, column=0)

        home_text = tk.Label(window, text="Homogeneity Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        home_text.grid(row=3, column=1)

        contrast_text = tk.Label(window, text="Contrast Based Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        contrast_text.grid(row=3, column=2)

        image_9x9_text = tk.Label(window, text="9x9 Mask Image ", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        image_9x9_text.grid(row=3, column=3)


   else:
        messagebox.showerror("Error", "Please upload an image first.")
