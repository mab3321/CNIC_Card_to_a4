from PIL import Image,ImageOps
import numpy as np
import cv2
# Define the A4 paper size at 300 dpi
A4_WIDTH = 2480
A4_HEIGHT = 3508

# Define the margin and spacing in inches, then convert to pixels
MARGIN_INCHES = 0.2
SPACING_INCHES = 0.1
MARGIN = int(MARGIN_INCHES * 300)  # 0.2 inches in pixels
SPACING = int(SPACING_INCHES * 300)  # 0.1 inches in pixels

def process_image(file_path):
    # Open the uploaded image
    with Image.open(file_path) as img:
        # Convert the image to a numpy array
        img_np = np.array(img)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

        # Apply threshold to get a binary image
        _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Sort contours by area and ignore small ones
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        # Assume the largest contour is the ID card
        cnt = contours[0]

        # Compute the bounding rectangle for the contour
        x, y, w, h = cv2.boundingRect(cnt)
        # Crop the image to the bounding rectangle
        id_card = img_np[y:y+h, x:x+w]

        # Convert numpy array back to PIL image
        id_card_img = Image.fromarray(id_card)

        # Calculate new width and height with spacing
        new_width = (A4_WIDTH - 2 * MARGIN - SPACING) // 2
        new_height = (A4_HEIGHT - 2 * MARGIN - 3 * SPACING) // 4

        # Resize the ID card image to fit the new dimensions
        resized_id_card_img = ImageOps.contain(id_card_img, (new_width, new_height))

        # Create a new blank A4 image with a white background
        a4_image = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')

        # Paste the resized ID card image into the A4 image 8 times to form a 2x4 grid with margins and spacing
        for i in range(4):  # Rows
            for j in range(2):  # Columns
                position = (
                    MARGIN + j * (new_width + SPACING),
                    MARGIN + i * (new_height + SPACING)
                )
                a4_image.paste(resized_id_card_img, position)

        return a4_image

# List of image file paths
image_files = [r"C:\Users\MAB\Downloads\CNIC_F.jpg", r"C:\Users\MAB\Downloads\CNIC_B.jpg"]  # Add your file paths here

# Create a PDF file
pdf_path = 'output.pdf'
a4_images = []

# Process each image and add it to the list
for image_file in image_files:
    a4_image = process_image(image_file)
    a4_images.append(a4_image)

# Save all A4 images into a single PDF file
a4_images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=a4_images[1:])
