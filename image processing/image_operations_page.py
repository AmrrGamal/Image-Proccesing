import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import sys
sys.path.append(r'C:\Users\Ms\Desktop\image processing\image operations')
from add import display_add_result
from sub import display_sub_result
from cut_paste import display_cut_paste_result
from invert import display_invert_result


def open_image_operations_page():
    uploaded_image_1 = None
    uploaded_image_2 = None

    def upload_image_1():
        nonlocal uploaded_image_1
        file_path = filedialog.askopenfilename(
            parent=new_window,
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if file_path:
            uploaded_image_1 = Image.open(file_path)
            image = uploaded_image_1.resize((200, 200))  
            photo = ImageTk.PhotoImage(image)
            image_label_1.config(image=photo)
            image_label_1.image = photo

    def upload_image_2():
        nonlocal uploaded_image_2
        file_path = filedialog.askopenfilename(
            parent=new_window,
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if file_path:
            uploaded_image_2 = Image.open(file_path)
            image = uploaded_image_2.resize((200, 200))  
            photo = ImageTk.PhotoImage(image)
            image_label_2.config(image=photo)
            image_label_2.image = photo

    def show_add_result():
        if uploaded_image_1 and uploaded_image_2:
            added_image = display_add_result(new_window,uploaded_image_1, uploaded_image_2)
            added_image_resized = added_image.resize((550, 350))  
            display_photo = ImageTk.PhotoImage(added_image_resized)
            result_label.config(image=display_photo)
            result_label.image = display_photo
        else:
            new_window.after(10, lambda: messagebox.showinfo("No Image", "Both images must be uploaded before addition.", parent=new_window))

    def show_sub_result():
        if uploaded_image_1 and uploaded_image_2:
            sub_image = display_sub_result(new_window, uploaded_image_1, uploaded_image_2)
            if sub_image is None:
                print("Error: The subtraction result is None.")
                return
            
            sub_image_resized = sub_image.resize((550, 350)) 
            display_photo = ImageTk.PhotoImage(sub_image_resized)
            result_label.config(image=display_photo)
            result_label.image = display_photo
        else:
            new_window.after(10, lambda: messagebox.showinfo("No Image", "Both images must be uploaded before subtraction.", parent=new_window))


    def show_threshold_input_box(): 
        input_window = tk.Toplevel()
        input_window.title("Enter Cutting Parameters")
        input_window.geometry("400x400")
        input_window.config(bg="#f0f8ff")

        
        input_window.update_idletasks()
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()
        window_width = 400
        window_height = 400
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        input_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


        tk.Label(input_window, text="Cut Position X:", font=("Arial", 12), bg="#f0f8ff").pack(pady=5)
        cut_position_X_entry = tk.Entry(input_window, font=("Arial", 12))
        cut_position_X_entry.pack(pady=5)

        tk.Label(input_window, text="Cut Position Y:", font=("Arial", 12), bg="#f0f8ff").pack(pady=5)
        cut_position_Y_entry = tk.Entry(input_window, font=("Arial", 12))
        cut_position_Y_entry.pack(pady=5)

        tk.Label(input_window, text="Cut Size Width:", font=("Arial", 12), bg="#f0f8ff").pack(pady=5)
        cut_size_W_entry = tk.Entry(input_window, font=("Arial", 12))
        cut_size_W_entry.pack(pady=5)

        tk.Label(input_window, text="Cut Size Height:", font=("Arial", 12), bg="#f0f8ff").pack(pady=5)
        cut_size_H_entry = tk.Entry(input_window, font=("Arial", 12))
        cut_size_H_entry.pack(pady=5)

        def submit_thresholds():
            try:
                cut_position_X = int(cut_position_X_entry.get())
                cut_position_Y = int(cut_position_Y_entry.get())
                cut_size_W = int(cut_size_W_entry.get())
                cut_size_H = int(cut_size_H_entry.get())

                if cut_position_X >= 0 and cut_position_Y >= 0 and cut_size_W > 0 and cut_size_H > 0:
                    show_cut_paste_result(cut_position_X, cut_position_Y, cut_size_W, cut_size_H)
                    input_window.destroy()  
                else:
                    new_window.after(10, lambda: messagebox.showinfo("Invalid Input", "All values must be positive integers", parent=new_window))
            except ValueError:
                new_window.after(10, lambda: messagebox.showinfo("Invalid Input", "Please enter valid integers for all fields", parent=new_window))

        submit_button = tk.Button(input_window, text="Submit", command=submit_thresholds, bg="#4a90e2", fg="white", font=("Arial", 14))
        submit_button.pack(pady=10)        

    def show_cut_paste_result( cut_position_X,cut_position_Y, cut_size_W,cut_size_H):
        if uploaded_image_1 and uploaded_image_2:
            sub_image = display_cut_paste_result(new_window, uploaded_image_1, uploaded_image_2, cut_position_X,cut_position_Y, cut_size_W,cut_size_H)

            if sub_image is None:
                print("Error: The subtraction result is None.")
                return
            
            sub_image_resized = sub_image.resize((550, 350)) 
            display_photo = ImageTk.PhotoImage(sub_image_resized)

            result_label.config(image=display_photo)
            result_label.image = display_photo
        else:
            new_window.after(10, lambda: messagebox.showinfo("No Image", "Both images must be uploaded before cut and paste", parent=new_window))


    def show_invert_result():
        if uploaded_image_1:
            invert_image = display_invert_result(new_window, uploaded_image_1)

            if invert_image is None:
                print("Error: Inversion result is None.")
                return 

            invert_image_resized = invert_image.resize((550, 350))
            display_photo = ImageTk.PhotoImage(invert_image_resized)

            result_label.config(image=display_photo)
            result_label.image = display_photo
        else:
            new_window.after(10, lambda: messagebox.showinfo("No Image", "Both images must be uploaded before invert", parent=new_window))
           
    new_window = tk.Toplevel()
    new_window.title("Image Operations")
    new_window.geometry("800x600")
    new_window.config(bg="#f0f8ff")

    window_width = 1300
    window_height = 730
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    position_top = (screen_height // 2) - (window_height // 2)
    position_left = (screen_width // 2) - (window_width // 2)

    new_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    label = tk.Label(new_window, text=" Image Operations ", font=("Arial", 18, "bold"), fg="#4a90e2", bg="#f0f8ff")
    label.pack(pady=20)

    frame = tk.Frame(new_window, bg="#f0f8ff")
    frame.pack(pady=20)

    upload_button_1 = tk.Button(frame, text="Upload Image 1", command=upload_image_1, bg="#4a90e2", fg="white", font=("Arial", 13), width=15)
    upload_button_1.grid(row=0, column=0, padx=10, pady=10)

    image_label_1 = tk.Label(frame, bg="#f0f8ff")
    image_label_1.grid(row=1, column=0, pady=10)

    frame.grid_columnconfigure(1, minsize=100)

    upload_button_2 = tk.Button(frame, text="Upload Image 2", command=upload_image_2, bg="#4a90e2", fg="white", font=("Arial", 13), width=15)
    upload_button_2.grid(row=0, column=3, padx=10, pady=10)

    image_label_2 = tk.Label(frame, bg="#f0f8ff")
    image_label_2.grid(row=1, column=3, pady=10)

    process_frame = tk.Frame(new_window, bg="#f0f8ff")
    process_frame.pack(pady=20)

    button = tk.Button(process_frame, text="Add ",  command=show_add_result, bg="#4a90e2", fg="white", font=("Arial", 12), width=12)
    button.grid(row=5, column=0, padx=85)

    button_2 = tk.Button(process_frame, text="Substract", command=show_sub_result, bg="#4a90e2", fg="white", font=("Arial", 12), width=12)
    button_2.grid(row=5, column=1, padx=85)

    process_frame.grid_rowconfigure(5, minsize=40)
    process_frame.grid_rowconfigure(6, minsize=40)

    button_3 = tk.Button(process_frame, text="Cut and Paste", command=show_threshold_input_box, bg="#4a90e2", fg="white", font=("Arial", 12), width=12)
    button_3.grid(row=6, column=0, padx=10, pady=20)

    button_4 = tk.Button(process_frame, text="Invert", command=show_invert_result, bg="#4a90e2", fg="white", font=("Arial", 12), width=12)
    button_4.grid(row=6, column=1, padx=10, pady=20)

    result_label = tk.Label(new_window, bg="#f0f8ff")
    result_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    open_image_operations_page()
    root.mainloop()
