import os
from PIL import Image

def combine_images(folder_path):
    # Get all image filenames in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Sort filenames numerically
    image_files.sort(key=lambda x: int(os.path.splitext(x)[0]))

    # Group images in sets of three
    for i in range(0, len(image_files), 3):
        group = image_files[i:i+3]

        if len(group) < 3:
            print(f"Skipping group {group} as it has less than 3 images.")
            continue

        # Open images
        images = [Image.open(os.path.join(folder_path, img)) for img in group]

        # Calculate total width and max height
        total_width = sum(img.width for img in images)
        max_height = max(img.height for img in images)

        # Create a new blank image
        combined_image = Image.new('RGB', (total_width, max_height))

        # Paste images side by side
        x_offset = 0
        for img in images:
            combined_image.paste(img, (x_offset, 0))
            x_offset += img.width

        # Save the combined image
        output_filename = f"combined_{i//3 + 1}.jpg"
        combined_image.save(os.path.join(folder_path, output_filename))
        print(f"Saved combined image: {output_filename}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing images: ")
    combine_images(folder_path)