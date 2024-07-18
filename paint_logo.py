from PIL import Image


def convert_non_white_to_black(image_path, output_path):
    # Open the image
    img = Image.open(image_path).convert("RGBA")  # Ensure the image is in RGBA format

    # Load the pixel data
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            # Check if the pixel is not white
            if (r, g, b) != (255, 255, 255):
                # Convert to black
                pixels[x, y] = (0, 0, 0, a)

    # Save the modified image
    img.save(output_path)


def leave_only_same(source_1, source_2, result):
    # Open the image
    img1 = Image.open(source_1).convert("RGBA")  # Ensure the image is in RGBA format
    img2 = Image.open(source_2).convert("RGBA")  # Ensure the image is in RGBA format

    # Load the pixel data
    pixels1 = img1.load()
    pixels2 = img2.load()

    # Get image dimensions
    width, height = img1.size

    # Create a new blank image for the result
    result_img = Image.new("RGBA", (width, height))

    # Load the pixel data for the result image
    result_pixels = result_img.load()

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            r1, g1, b1, a1 = pixels1[x, y]
            r2, g2, b2, a2 = pixels2[x, y]

            # Check if the pixel is not white
            if (r1, g1, b1) == (r2, g2, b2):
                # Convert to white
                result_pixels[x, y] = (r1, g1, b1, a1)

        # Save the modified image
    result_img.save(result)


def remove_dark_pixels(source, result):
    # Open the image
    img = Image.open(source).convert("RGBA")  # Ensure the image is in RGBA format

    # Load the pixel data
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Create a new blank image for the result
    result_img = Image.new("RGBA", (width, height))

    # Load the pixel data for the result image
    result_pixels = result_img.load()

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            # Check if the pixel is not white
            if r > 80 and g > 80 and b > 80:
                # Convert to white
                result_pixels[x, y] = (r, g, b, a)

        # Save the modified image
    result_img.save(result)

def convert_all_to_black(image_path, output_path):
    # Open the image
    img = Image.open(image_path).convert("RGBA")  # Ensure the image is in RGBA format

    # Load the pixel data
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            # Convert to black
            pixels[x, y] = (0, 0, 0, a)

    # Save the modified image
    img.save(output_path)

def convert_all_to_white(image_path, output_path):
    # Open the image
    img = Image.open(image_path).convert("RGBA")  # Ensure the image is in RGBA format

    # Load the pixel data
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            # Convert to black
            pixels[x, y] = (255, 255, 255, a)

    # Save the modified image
    img.save(output_path)



if __name__ == '__main__':
    # Example usage
    # leave_only_same("source1.png", "source2.png", "result.png")
    # remove_dark_pixels("logo.png", "clear_logo2.png")
    convert_all_to_white("static/assets/clear_logo.png", "static/assets/white_logo.png")
