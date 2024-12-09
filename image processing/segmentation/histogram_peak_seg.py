
import numpy as np
from PIL import Image
from histogram import calculate_histogram
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox 
import numpy as np
from PIL import Image



def histogram_peak_threshold_segmentation(image):
    if image.mode != 'L':
        image = image.convert('L')
    
    img_array = np.array(image, dtype=np.uint8)

    hist, bins = calculate_histogram(image) 
    peaks_indices = find_peaks_and_sort_them(hist)

    if len(peaks_indices) < 2:
        low_threshold, high_threshold = 0, 255 
    else:
        low_threshold, high_threshold = calculate_low_and_high_thresholds(peaks_indices)
        print(f" low threshold: {low_threshold},  high threshold: {high_threshold}")

    segmented_image = np.zeros_like(img_array)
    segmented_image[(img_array >= low_threshold) & (img_array <= high_threshold)] = 255

    return Image.fromarray(segmented_image)


def find_peaks_and_sort_them(hist):
    peaks = find_peaks_from_histogram(hist, height=0)
    if len(peaks) == 0:
        peaks = [0, len(hist) - 1] 

    sorted_peaks = sorted(peaks, key=lambda x: hist[x], reverse=True)
    return sorted_peaks[:2]


def calculate_low_and_high_thresholds(peaks_indices):

    peak1 = peaks_indices[0]
    peak2 = peaks_indices[1]
 
    low_threshold = (peak1 + peak2) // 2
    high_threshold = peak2

    return low_threshold, high_threshold


def find_peaks_from_histogram(hist, height=0):
    peaks = []
    hist = np.array(hist)
    for i in range(1, len(hist) - 1):
        if hist[i] > hist[i - 1] and hist[i] > hist[i + 1]:
            if hist[i] >= height:
                peaks.append(i) 
    
    if hist[0] > hist[1] and hist[0] >= height:
        peaks.insert(0, 0)  
    if hist[-1] > hist[-2] and hist[-1] >= height:
        peaks.append(len(hist) - 1)  

    return peaks




def display_peak_segmetation_result(master, original_image):
    if original_image:
        window = tk.Toplevel(master)
        window.title("Peak Segmetation Result")
       
        window.configure(bg="#f0f8ff")
        
        window_width = 900
        window_height = 500
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        position_top = (screen_height // 2) - (window_height // 2)
        position_left = (screen_width // 2) - (window_width // 2)
        
        window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        peak_seg_image = histogram_peak_threshold_segmentation(original_image)

        if peak_seg_image:
            original_resized = ImageTk.PhotoImage(original_image.resize((400, 300)))
            peak_seg_resized = ImageTk.PhotoImage(peak_seg_image.resize((400, 300)))

            main_title = tk.Label(window, text="Peak Segmentation Result", font=("Arial", 18, "bold"), fg="#4a90e2", bg="#f0f8ff")
            main_title.grid(row=0, column=0,  columnspan=2, pady=(10, 0))

            original_label = tk.Label(window, image=original_resized)
            original_label.image = original_resized
            original_label.grid(row=1, column=0, padx=20, pady=20)

            label = tk.Label(window, image=peak_seg_resized)
            label.image = peak_seg_resized
            label.grid(row=1, column=1, padx=20, pady=20)

            original_text = tk.Label(window, text="Original Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            original_text.grid(row=2, column=0)

            text = tk.Label(window, text="Peak Segmented Image", font=("Arial", 14, "bold"), fg="#4a90e2", bg="#f0f8ff")
            text.grid(row=2, column=1)

            back_button = tk.Button(window, text="Back to Upload", command=window.destroy, bg="#4a90e2", fg="white", font=("Arial", 14))
            back_button.grid(row=3, column=0, columnspan=2, pady=20)

    else:
        messagebox.showerror("Error", "Please upload an image first.")

