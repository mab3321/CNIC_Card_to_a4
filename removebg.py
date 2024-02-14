from rembg import remove
from PIL import Image
import numpy as np
import os
import cv2

def remove_background(input_path, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process the image to remove the background
    image = Image.open(input_path).convert("RGBA")
    output = remove(image)
    
    # Convert the output to numpy array
    img_np = np.array(output)
    
    # Assuming rembg returns an image where the background is already removed
    # Find the bounding box of the non-transparent pixels
    non_transparent_mask = img_np[:, :, 3] > 0
    bbox = Image.fromarray(non_transparent_mask).getbbox()
    
    # Crop the image to the bounding box
    id_card_img = output.crop(bbox)
    
    # Construct the output path
    filename = os.path.basename(input_path)
    basename, _ = os.path.splitext(filename)
    output_path = os.path.join(output_dir, basename + '.png')
    
    # Save the image without background
    id_card_img.save(output_path, 'PNG')
    print(f"Processed: {output_path}")

# List of image file paths
image_files = [
    r"C:\Users\MAB\Downloads\CNIC_B.jpg",
    r"C:\Users\MAB\Downloads\CNIC_F.jpg"
    # Add other image paths here
]

# Define the directory where to save the output images
output_directory = r"C:\Users\MAB\Downloads\Processed_Images"

# Process each image in the list
for image_path in image_files:
    remove_background(image_path, output_directory)
