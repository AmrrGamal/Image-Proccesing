import tkinter as tk
from tkinter import filedialog ,simpledialog ,messagebox
from PIL import Image, ImageTk
import sys
sys.path.append(r'C:\Users\Ms\Desktop\image processing\Halftone and Histogram')
sys.path.append(r'C:\Users\Ms\Desktop\image processing\All Basic Edge Detection')
sys.path.append(r'C:\Users\Ms\Desktop\image processing\All Advanced Edge Detection')
sys.path.append(r'C:\Users\Ms\Desktop\image processing\Spatail Frequancy')
sys.path.append(r'C:\Users\Ms\Desktop\image processing\segmentation')
sys.path.append(r'C:\Users\Ms\Desktop\image processing\Helper')
from avg_image_threshold import calculate_average_threshold
from histogram import plot_histogram_tk ,calculate_histogram
from advanced_halftone import display_advanced_halftoning_result
from simple_halftone import display_simple_halftoning_result
from sobel import display_sobel_result
from prewit import display_prewit_result
from kirsch import display_kirsch_result
from all_basic_edge_detection import display_all_basic_result
from hist_equalization import display_hist_eq_result
from homogeneity import display_homogeneity_result
from difference import display_difference_result
from variance import display_variance_result
from contrast_based import display_contrast_based_result
from dog import display_dog_result
from range import display_range_result
from all_advanced import display_all_advanced_result
from high_pass import display_high_pass_filter_result
from low_pass import display_low_pass_filter_result
from mediam_filter import display_median_filter_result
from all_spatail_filters import display_all_spatail_filters_result
from image_operations_page import open_image_operations_page
from manual_seg import display_manual_segmentation_result
from histogram_peak_seg import display_peak_segmetation_result
from histogram_valley_seg import display_valley_segmetation_result
from histogram_adaptive_seg import display_adaptive_segmetation_result
from All_Basic_seg_techs import display_all_basic_seg_result



class ImageProcessingApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Processing Project") 
        master.geometry("1040x1040")  
        master.config(bg="#f0f8ff")  

        self.scroll(master)

        self.header = tk.Label(self.container, text="Image Processing Techniques", font=("Arial", 20, "bold"), fg="#4a90e2", bg="#f0f8ff")
        self.header.pack(pady=0)

        self.upload_button = tk.Button(self.container, text="Upload Image", command=self.upload_image, bg="#4a90e2", fg="white", font=("Arial", 16), width=20)
        self.upload_button.pack(pady=10)

        self.upload_message = tk.Label(self.container, text="Please upload an image", font=("Arial", 16, "bold"), fg="#4a90e2", bg="#f0f8ff")
        self.upload_message.pack(pady=20)

        self.image_label = tk.Label(self.container)
        self.image_label.pack()

        self.process_frame = tk.Frame(self.container, bg="#f0f8ff")  
        self.process_frame.pack(pady=30)

        self.buttons()
        
        self.original_image = None
        self.display_image = None      



    def scroll(self, master):
        self.canvas = tk.Canvas(master, bg="#f0f8ff", highlightthickness=0)  
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.container = tk.Frame(self.canvas, width=800, height=1500, bg="#f0f8ff", 
                                  padx=30, pady=30, bd=0, relief="flat") 
        self.canvas.create_window((700, 700), window=self.container, anchor="nw")  

        self.container.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all"))) 

    def buttons(self):
        self.halftoning_button_1 = tk.Button(self.process_frame, text="Simple Halftone", command=self.show_simple_halftoning_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.halftoning_button_1.grid(row=0, column=0,padx=15, pady=20)

        self.halftoning_button_2 = tk.Button(self.process_frame, text="Advance Halftone", command=self.show_advanced_halftoning_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.halftoning_button_2.grid(row=0, column=2,padx=15, pady=20)

        self.Histogram_button_1 = tk.Button(self.process_frame, text="Histogram", command=self.show_histogram_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Histogram_button_1.grid(row=1, column=0, padx=45, pady=20)

        self.hist_eq = tk.Button(self.process_frame, text="Equalization", command=self.show_hist_eq_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.hist_eq.grid(row=1, column=2, padx=45, pady=20)

        self.sobel = tk.Button(self.process_frame, text="Sobel", command=self.show_sobel_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.sobel.grid(row=2, column=0, padx=10, pady=20)

        self.Prewit = tk.Button(self.process_frame, text="Prewit", command=self.show_prewit_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Prewit.grid(row=2, column=1, padx=10, pady=20)

        self.Kisch = tk.Button(self.process_frame, text="Kirsch", command=self.show_kirsch_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Kisch.grid(row=2, column=2, padx=10, pady=20)

        self.All_Basic = tk.Button(self.process_frame, text="All Basic Edge Detection Techniques ", command=self.show_all_basic_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=54)
        self.All_Basic.grid(row=3, column=0, columnspan=3, padx=10, pady=20) 

        self.Homogeneity = tk.Button(self.process_frame, text="Homogeneity", command=self.show_home_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Homogeneity.grid(row=4, column=0, padx=10, pady=20)

        self.Difference = tk.Button(self.process_frame, text="Difference", command=self.show_diff_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Difference.grid(row=4, column=2, padx=10, pady=20)
        
        self.DOG = tk.Button(self.process_frame, text="DOG", command=self.show_dog_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.DOG.grid(row=5, column=0, padx=10, pady=20)

        self.Variance = tk.Button(self.process_frame, text="Variance", command=self.show_variance_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Variance.grid(row=5, column=2, padx=10, pady=20)

        self.Range = tk.Button(self.process_frame, text="Range", command=self.show_range_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Range.grid(row=6, column=0, padx=10, pady=20)

        self.Contrast = tk.Button(self.process_frame, text="Contrast", command=self.show_contrast_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Contrast.grid(row=6, column=2, padx=10, pady=20)

        self.All_Basic_edge_detection = tk.Button(self.process_frame, text="All Advanced Edge Detection Techniques ", command=self.show_all_advanced_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=54)
        self.All_Basic_edge_detection.grid(row=7, column=0, columnspan=3, padx=10, pady=20)
       
        self.manual_seg = tk.Button(self.process_frame, text="Manual Segment", command=self.show_threshold_input_box, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.manual_seg.grid(row=8, column=0, padx=10, pady=20)

        self.peak_seg = tk.Button(self.process_frame, text="Peak Segment", command=self.show_display_peak_segmentation_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.peak_seg.grid(row=8, column=2, padx=10, pady=20)

        self.valley_seg = tk.Button(self.process_frame, text="Valley Segment", command=self.show_display_valley_segmentation_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.valley_seg.grid(row=9, column=0, padx=10, pady=20)

        self.adaptive_seg = tk.Button(self.process_frame, text="Adaptive Segment", command=self.show_display_adaptive_segmentation_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.adaptive_seg.grid(row=9, column=2, padx=10, pady=20)

        self.All_Basic_seg = tk.Button(self.process_frame, text="All Basic Segmentation Techniques ", command=self.show_display_all_basic_seg_segmentation_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=54)
        self.All_Basic_seg.grid(row=10, column=0, columnspan=3, padx=10, pady=20)

        self.High_Pass = tk.Button(self.process_frame, text="High Pass Filter", command=self.show_high_pass_filter_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.High_Pass.grid(row=11, column=0, padx=10, pady=20)

        self.Low_Pass = tk.Button(self.process_frame, text="Low Pass Filter", command=self.show_low_pass_filter_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Low_Pass.grid(row=11, column=2, padx=10, pady=20)

        self.Median = tk.Button(self.process_frame, text="Median Filter", command=self.show_median_filter_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=14)
        self.Median.grid(row= 11, column=1, padx=10, pady=20)

        self.Spatial_Frequency_Filters = tk.Button(self.process_frame, text="All Spatial Frequency Filters", command=self.show_all_spatail_filters_result, bg="#4a90e2", fg="white", font=("Arial", 14), width=54)
        self.Spatial_Frequency_Filters.grid(row=12, column=0, columnspan=3, padx=10, pady=20)

        self.Image_Operations = tk.Button(self.process_frame, text="Image Operations", command=open_image_operations_page, bg="#4a90e2", fg="white", font=("Arial", 14), width=54)
        self.Image_Operations.grid(row=13, column=0, columnspan=3, padx=10, pady=20)

     
    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if file_path:
            self.upload_message.pack_forget()
            self.original_image = Image.open(file_path)
            self.display_image = ImageTk.PhotoImage(self.original_image.resize((600, 350)))
            self.image_label.config(image=self.display_image)
            self.image_label.pack()

    def show_advanced_halftoning_result(self):
        if self.original_image:
            halftoned_image = display_advanced_halftoning_result(self.master, self.original_image)  
            self.display_image = ImageTk.PhotoImage(halftoned_image.resize((550, 350)))
            self.image_label.config(image=self.display_image)
        else:
           messagebox.showinfo("No Image", "Please upload an image first")    

    def show_simple_halftoning_result(self):
        if self.original_image:
            halftoned_image = display_simple_halftoning_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(halftoned_image.resize((550, 350)))
            self.image_label.config(image=self.display_image)
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      

    def show_histogram_result(self):
        if self.original_image:
            histogram ,bin=calculate_histogram(self.original_image)
            halftoned_image = plot_histogram_tk(self.master, histogram)  
            self.display_image = ImageTk.PhotoImage(halftoned_image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")             

    def show_sobel_result(self):
        if self.original_image:
            image = display_sobel_result(self.master, self.original_image)  
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      


    def show_prewit_result(self):
        if self.original_image:
            image = display_prewit_result(self.master, self.original_image)  
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      


    def show_kirsch_result(self):
        if self.original_image:
            image = display_kirsch_result(self.master, self.original_image)  
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)
        else:
           messagebox.showinfo("No Image", "Please upload an image first")        

    def show_home_result(self):
        if not self.original_image:
            messagebox.showinfo("No Image", "Please upload an image first")
            return
        
        response = messagebox.askyesno("Threshold", "What do you want to use as threshold?\n\nClick 'Yes' for Manual Threshold\n\nClick 'No' for Avarage Threshold")

        if response: 
            threshold = simpledialog.askfloat("Input Threshold", "Enter the manual threshold value:", minvalue=0.0, maxvalue=255.0)
            if threshold is not None:
                processed_image = display_homogeneity_result(self.master, self.original_image, threshold)
        else:  
            threshold = calculate_average_threshold(self.original_image)
            processed_image = display_homogeneity_result(self.master, self.original_image, threshold)

        self.display_image = ImageTk.PhotoImage(processed_image.resize((550, 350)))
        self.image_label.config(image=self.display_image)


    def show_diff_result(self):
        if not self.original_image:
            messagebox.showinfo("No Image", "Please upload an image first")
            return
        
        response = messagebox.askyesno("Threshold", "What do you want to use as threshold?\n\nClick 'Yes' for Manual Threshold\n\nClick 'No' for Avarage Threshold")

        if response: 
            threshold = simpledialog.askfloat("Input Threshold", "Enter the manual threshold value:", minvalue=0.0, maxvalue=255.0)
            if threshold is not None:
                processed_image = display_difference_result(self.master, self.original_image, threshold)
        else:  
            threshold = calculate_average_threshold(self.original_image)
            processed_image = display_difference_result(self.master, self.original_image, threshold)

        self.display_image = ImageTk.PhotoImage(processed_image.resize((550, 350)))
        self.image_label.config(image=self.display_image)    

    def show_hist_eq_result(self):
        if self.original_image:
            image = display_hist_eq_result(self.master, self.original_image)  
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      

    def show_range_result(self):
        if self.original_image:
            image = display_range_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      

    def show_variance_result(self):
        if self.original_image:
            image = display_variance_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)  
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      

    def show_dog_result(self):
        if self.original_image:
            image = display_dog_result(self.master, self.original_image)  
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")         

    def show_contrast_result(self):
        if self.original_image:
            image = display_contrast_based_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")       
    
    def show_all_basic_result(self):
        if self.original_image:
            image = display_all_basic_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      

    def show_all_advanced_result(self):
        if self.original_image:
            image = display_all_advanced_result(self.master, self.original_image)  
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")        

    def show_high_pass_filter_result(self):
        if self.original_image:
            image = display_high_pass_filter_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")       

    def show_low_pass_filter_result(self):
        if self.original_image:
            image = display_low_pass_filter_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)  
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      

    def show_median_filter_result(self):
        if self.original_image:
            image = display_median_filter_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")       


    def show_all_spatail_filters_result(self):
        if self.original_image:
            image = display_all_spatail_filters_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image) 
        else:
           messagebox.showinfo("No Image", "Please upload an image first")         

    def show_threshold_input_box(self):
        
        input_window = tk.Toplevel(self.master)
        input_window.title("Enter Thresholds")
        input_window.geometry("300x200")
        input_window.config(bg="#f0f8ff")

        input_window.update_idletasks()
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()
        window_width = 300
        window_height = 200
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        input_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
       
        low_label = tk.Label(input_window, text="Low Threshold (0-255):", font=("Arial", 12), bg="#f0f8ff")
        low_label.pack(pady=5)
        
        low_entry = tk.Entry(input_window, font=("Arial", 12))
        low_entry.pack(pady=5)
        
        high_label = tk.Label(input_window, text="High Threshold (0-255):", font=("Arial", 12), bg="#f0f8ff")
        high_label.pack(pady=5)
        
        high_entry = tk.Entry(input_window, font=("Arial", 12))
        high_entry.pack(pady=5)
        
        def submit_thresholds():
            try:
                low_threshold = int(low_entry.get())
                high_threshold = int(high_entry.get())
                if(low_threshold<high_threshold):
                    if 0 <= low_threshold <= 255 and 0 <= high_threshold <= 255:
                        self.show_display_manual_segmentation_result(low_threshold, high_threshold)
                        input_window.destroy() 
                    else:
                        messagebox.showerror("Invalid Input", "Thresholds must be between 0 and 255.")
                else:
                    messagebox.showerror("Invalid Input", "High Thresholds must be Must be greater then Low Threshold")         
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid integers for both thresholds.")
        
        submit_button = tk.Button(input_window, text="Submit", command=submit_thresholds, bg="#4a90e2", fg="white", font=("Arial", 14))
        submit_button.pack(pady=10)

    def show_display_manual_segmentation_result(self, low_threshold, high_threshold):
        if self.original_image:
            image = display_manual_segmentation_result(self.master, self.original_image, low_threshold, high_threshold) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)  
        else:
           messagebox.showinfo("No Image", "Please upload an image first")          
     
    def show_display_peak_segmentation_result(self):
        if self.original_image:
            image = display_peak_segmetation_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)  
        else:
           messagebox.showinfo("No Image", "Please upload an image first")      

    def show_display_valley_segmentation_result(self):
        if self.original_image:
            image = display_valley_segmetation_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)  
        else:
           messagebox.showinfo("No Image", "Please upload an image first")       

    
    def show_display_adaptive_segmentation_result(self):
        if self.original_image:
            image = display_adaptive_segmetation_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)  
        else:
           messagebox.showinfo("No Image", "Please upload an image first")       

    def show_display_all_basic_seg_segmentation_result(self):
        if self.original_image:
            image = display_all_basic_seg_result(self.master, self.original_image) 
            self.display_image = ImageTk.PhotoImage(image.resize((550, 350)))
            self.image_label.config(image=self.display_image)  
        else:
           messagebox.showinfo("No Image", "Please upload an image first")                                                                     
    

root = tk.Tk()
app = ImageProcessingApp(root)
root.mainloop()
