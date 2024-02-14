from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process the image to remove the background
    image = Image.open(input_path)
    output = remove(image)
    
    # Construct the output path
    filename = os.path.basename(input_path)
    filename = filename.split(".")[0] + ".png"  
    output_path = os.path.join(output_dir, filename)
    
    # Save the image without background
    output.save(output_path)
    print(f"Processed: {output_path}")

# List of image file paths
image_files = [
    r"C:\Users\MAB\Downloads\CNIC_B.jpg",
    r"C:\Users\MAB\Downloads\CNIC_F.jpg"
    # Add other image paths here
]

# Define the directory where to save the output images
output_directory = r"./"

# Process each image in the list
for image_path in image_files:
    remove_background(image_path, output_directory)
