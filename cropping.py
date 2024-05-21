from PIL import Image

def crop_image(image, crop_left, crop_top, crop_width, crop_height):
    # Create a new image for the cropped area
    cropped_image = Image.new('RGB', (crop_width, crop_height))
    
    # Get pixel data
    pixels = image.load()
    cropped_pixels = cropped_image.load()
    
    # Loop through each pixel in the cropped area
    for y in range(crop_height):
        for x in range(crop_width):
            original_x = crop_left + x
            original_y = crop_top + y
            
            # Check if the original coordinates are within the bounds of the image
            if 0 <= original_x < image.width and 0 <= original_y < image.height:
                cropped_pixels[x, y] = pixels[original_x, original_y]
    
    return cropped_image

# Load the image using Pillow (for demonstration purposes)
input_image = Image.open('image.jpg')

# Define crop region (left, top, width, height)
crop_left, crop_top, crop_width, crop_height = 500, 500, 500, 500

# Crop the image
cropped_image = crop_image(input_image, crop_left, crop_top, crop_width, crop_height)

# Save or display the result
cropped_image.save('cropped_image.jpg')
cropped_image.show()