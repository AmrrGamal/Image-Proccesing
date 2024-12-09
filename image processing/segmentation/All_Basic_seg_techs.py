import tkinter as tk 
from PIL import ImageTk
from tkinter import messagebox 
from manual_seg import manual_segmentation
from histogram_peak_seg import histogram_peak_threshold_segmentation
from histogram_valley_seg import histogram_valley_threshold_segmentation
from histogram_adaptive_seg import adaptive_histogram_threshold_segmentation

def all_basic_seg_techs(image):
   manual_seg_image = manual_segmentation(image,100, 200)
   peak_seg_image = histogram_peak_threshold_segmentation(image)
   valley_seg_image = histogram_valley_threshold_segmentation(image)
   adaptive_seg_image = adaptive_histogram_threshold_segmentation(image)

   return manual_seg_image, peak_seg_image, valley_seg_image, adaptive_seg_image
   

def display_all_basic_seg_result(master, original_image):
   if original_image:
        window = tk.Toplevel(master)
        window.title("All Basic Segmentation Techniques Result")
        window.configure(bg="#f0f8ff")
        
        window_width = 1300
        window_height = 730
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
        manual_seg_image, peak_seg_image, valley_seg_image, adaptive_seg_image = all_basic_seg_techs(original_image)

        original_resized = ImageTk.PhotoImage(original_image.resize((300, 240)))
        manual_seg_resized = ImageTk.PhotoImage(manual_seg_image.resize((300, 240)))
        peak_seg_resized = ImageTk.PhotoImage(peak_seg_image.resize((300, 240)))
        valley_seg_resized = ImageTk.PhotoImage(valley_seg_image.resize((300, 240)))
        adaptive_seg_resized = ImageTk.PhotoImage(adaptive_seg_image.resize((300, 240)))

        main_title = tk.Label(window, text="All Basic Segmentation Techniques Result", font=("Arial", 20, "bold"), fg="#4a90e2", bg="#f0f8ff")
        main_title.grid(row=0, column=1,  columnspan=1, pady=(10, 0)) 

        original_label = tk.Label(window, image=original_resized)
        original_label.image = original_resized
        original_label.grid(row=1, column=0, padx=35, pady=10)

        manual_seg_label = tk.Label(window, image=manual_seg_resized)
        manual_seg_label.image = manual_seg_resized
        manual_seg_label.grid(row=1, column=1, padx=0, pady=10)

        peak_seg_label = tk.Label(window, image=peak_seg_resized)
        peak_seg_label.image = peak_seg_resized
        peak_seg_label.grid(row=1, column=2, padx=0, pady=10)

        valley_seg_label = tk.Label(window, image=valley_seg_resized)
        valley_seg_label.image = valley_seg_resized
        valley_seg_label.grid(row=3, column=0, padx=35, pady=10)

        adaptive_seg_label = tk.Label(window, image=adaptive_seg_resized)
        adaptive_seg_label.image = adaptive_seg_resized
        adaptive_seg_label.grid(row=3, column=1, padx=0, pady=10)

        
        original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        original_text.grid(row=2, column=0)

        manual_seg_text = tk.Label(window, text="Manual Segmented Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        manual_seg_text.grid(row=2, column=1)

        peak_seg_text = tk.Label(window, text="Peak Segmented Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        peak_seg_text.grid(row=2, column=2)

        valley_seg_text = tk.Label(window, text="Valley Segmented Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        valley_seg_text.grid(row=4, column=0)

        adaptive_seg_text = tk.Label(window, text="Adaptive Segmented Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
        adaptive_seg_text.grid(row=4, column=1)
   else:
        messagebox.showerror("Error", "Please upload an image first.")
