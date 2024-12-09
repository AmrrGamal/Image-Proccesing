import tkinter as tk 
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image
from sobel import sobel_operator
from kirsch import kirsch_operator
from prewit import prewit_operator

def all_basic_operator(image):
   sobel_image = sobel_operator(image)
   prewit_image = prewit_operator(image)
   kirsch_image = kirsch_operator(image)
   
   return sobel_image, prewit_image, kirsch_image
   

def display_all_basic_result(master, original_image):
   if original_image:
        window = tk.Toplevel(master)
        window.title("All Basic Edge Detection Techniques Result")
        window.configure(bg="#f0f8ff")
        
        window_width = 1300
        window_height = 730
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        sobel_image, prewit_image, kirsch_image = all_basic_operator(original_image)

        original_resized = ImageTk.PhotoImage(original_image.resize((300, 240)))
        sobel_resized = ImageTk.PhotoImage(sobel_image.resize((300, 240)))
        prewit_resized = ImageTk.PhotoImage(prewit_image.resize((300, 240)))
        kirsch_resized = ImageTk.PhotoImage(kirsch_image.resize((300, 240)))

        main_title = tk.Label(window, text="All Basic Edge Detection Techniques Result", font=("Arial", 20, "bold"), fg="#4a90e2", bg="#f0f8ff")
        main_title.grid(row=0, column=1,  columnspan=1, pady=(10, 0)) 
        
        original_label = tk.Label(window, image=original_resized)
        original_label.image = original_resized
        original_label.grid(row=1, column=0,padx=30 , pady=10)

        sobel_label = tk.Label(window, image=sobel_resized)
        sobel_label.image = sobel_resized
        sobel_label.grid(row=1, column=1,  pady=10)

        prewit_label = tk.Label(window, image=prewit_resized)
        prewit_label.image = prewit_resized
        prewit_label.grid(row=1, column=2,  pady=10)

        kirsch_label = tk.Label(window, image=kirsch_resized)
        kirsch_label.image = kirsch_resized
        kirsch_label.grid(row=3, column=1,  pady=10)

        original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        original_text.grid(row=2, column=0)

        sobel_text = tk.Label(window, text="Sobel Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        sobel_text.grid(row=2, column=1)

        prewit_text = tk.Label(window, text="Prewitt Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        prewit_text.grid(row=2, column=2)

        kirsch_text = tk.Label(window, text="Kirsch Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        kirsch_text.grid(row=4, column=1)

   else:
        messagebox.showerror("Error", "Please upload an image first.")
