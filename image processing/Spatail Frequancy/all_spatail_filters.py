import tkinter as tk 
from PIL import ImageTk
from tkinter import messagebox 
from high_pass import high_pass_filter
from low_pass import low_pass_filter
from mediam_filter import median_filter

def all_spatail_filters(image):
   
   high_pass_image = high_pass_filter(image)
   low_pass_image = low_pass_filter(image)
   median_image = median_filter(image)

   return high_pass_image, low_pass_image, median_image
   

def display_all_spatail_filters_result(master, original_image):
   if original_image:
        window = tk.Toplevel(master)
        window.title("All Spatial Frequency Filters Result")
        window.geometry("1200x600")
        window.configure(bg="#f0f8ff")
             
        window_width = 1300
        window_height = 730

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        high_pass_image, low_pass_image, median_image = all_spatail_filters(original_image)

        original_resized = ImageTk.PhotoImage(original_image.resize((300, 240)))
        high_pass_resized = ImageTk.PhotoImage(high_pass_image.resize((300, 240)))
        low_pass_resized = ImageTk.PhotoImage(low_pass_image.resize((300, 240)))
        median_resized = ImageTk.PhotoImage(median_image.resize((300, 240)))

        main_title = tk.Label(window, text="All Spatial Frequency Filters Result", font=("Arial", 20, "bold"), fg="#4a90e2", bg="#f0f8ff")
        main_title.grid(row=0, column=1,  columnspan=1, pady=(10, 0)) 

        original_label = tk.Label(window, image=original_resized)
        original_label.image = original_resized
        original_label.grid(row=1, column=0, padx=60, pady=10)

        high_pass_label = tk.Label(window, image=high_pass_resized)
        high_pass_label.image = high_pass_resized
        high_pass_label.grid(row=1, column=1, pady=10)

        low_pass_label = tk.Label(window, image=low_pass_resized)
        low_pass_label.image = low_pass_resized
        low_pass_label.grid(row=1, column=2,  pady=10)

        median_label = tk.Label(window, image=median_resized)
        median_label.image = median_resized
        median_label.grid(row=3, column=1, pady=10)

        original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        original_text.grid(row=2, column=0)

        high_pass_text = tk.Label(window, text="High Pass Filter Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        high_pass_text.grid(row=2, column=1)

        low_pass_text = tk.Label(window, text="Low Pass Filter Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        low_pass_text.grid(row=2, column=2)

        medain_text = tk.Label(window, text="Medaim Filter Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        medain_text.grid(row=4, column=1)

  
   else:
        messagebox.showerror("Error", "Please upload an image first.")
