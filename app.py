from removebg import remove_background
from id_card_on_a4 import process_image

# List of image file paths
image_files = [
    r"C:\Users\MAB\Downloads\WhatsApp Image 2024-02-14 at 12.26.55_80159e97.jpg",
    r"C:\Users\MAB\Downloads\WhatsApp Image 2024-02-14 at 12.26.56_f9f4776c.jpg"
    # Add other image paths here
]

# Define the directory where to save the output images
RemoveBackGround = False
output_directory = r"C:\Users\MAB\Downloads\Processed_Images"
a4_images = []
# Process each image in the list
for image_path in image_files:
    if RemoveBackGround:
        output_path = remove_background(image_path, output_directory)
    else:
        output_path = image_path
    # Create a PDF file
    pdf_path = 'output.pdf'

    a4_image = process_image(output_path)
    a4_images.append(a4_image)
a4_images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=a4_images[1:])