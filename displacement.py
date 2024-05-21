from PIL import Image

def translate_image(image, tx, ty):
    width, height = image.size
    translated_image = Image.new('RGB', (width, height))
    
    # Get pixel data
    pixels = image.load()
    translated_pixels = translated_image.load()
    
    # Loop through each pixel in the original image
    for y in range(height):
        for x in range(width):
            new_x = x + tx
            new_y = y + ty
            
            # Check if the new coordinates are within the image bounds
            if 0 <= new_x < width and 0 <= new_y < height:
                translated_pixels[new_x, new_y] = pixels[x, y]
    
    return translated_image

# Load the image using Pillow (for demonstration purposes)
input_image = Image.open('image.jpg')

# Define translation values
tx, ty = 500, 300

# Translate the image
translated_image = translate_image(input_image, tx, ty)

# Save or display the result
translated_image.save('translated_image.jpg')
translated_image.show()