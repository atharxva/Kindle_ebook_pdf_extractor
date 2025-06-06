import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import sys
from datetime import datetime

def get_creation_time(filepath):
    # Get the creation time of the file
    return os.path.getctime(filepath)

def convert_images_to_pdf(input_folder, output_pdf):
    # Get all image files from the input folder
    image_files = []
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            full_path = os.path.join(input_folder, filename)
            image_files.append(full_path)
    
    if not image_files:
        print("No image files found in the specified folder!")
        return
    
    # Sort files by creation time
    image_files.sort(key=get_creation_time)
    
    # Create PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    
    print(f"Processing {len(image_files)} images...")
    
    for i, image_file in enumerate(image_files, 1):
        try:
            print(f"Processing image {i}/{len(image_files)}: {os.path.basename(image_file)}")
            
            # Open and resize image to fit the page
            with Image.open(image_file) as img:
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                    img = img.convert('RGB')
                
                img_width, img_height = img.size
                
                # Calculate scaling to fit the page while maintaining aspect ratio
                aspect = img_height / float(img_width)
                if aspect > 1:
                    # Portrait
                    img_width = width - 40
                    img_height = img_width * aspect
                else:
                    # Landscape
                    img_height = height - 40
                    img_width = img_height / aspect
                
                # Center the image on the page
                x = (width - img_width) / 2
                y = (height - img_height) / 2
                
                # Save image to temporary file
                temp_path = f"temp_{i}.jpg"
                img.save(temp_path, "JPEG", quality=95)
                
                # Draw the image
                c.drawImage(temp_path, x, y, width=img_width, height=img_height)
                c.showPage()
                
                # Clean up temporary file
                os.remove(temp_path)
                
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
            continue
    
    c.save()
    print(f"\nPDF created successfully: {output_pdf}")
    print(f"Total images processed: {len(image_files)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_to_pdf.py <input_folder> <output_pdf>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_pdf = sys.argv[2]
    
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist!")
        sys.exit(1)
    
    convert_images_to_pdf(input_folder, output_pdf) 