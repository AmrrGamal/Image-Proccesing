import numpy as np

def calculate_average_threshold(image):
    if image.mode != 'L':
        image = image.convert('L')
    img_array = np.array(image, dtype=np.float32)
    average_intensity = np.mean(img_array)
    return average_intensity 

