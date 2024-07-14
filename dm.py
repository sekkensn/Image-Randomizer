from PIL import Image
import random

def main():
    original_image_path = 'images/' + input("Enter the name image you want to edit: ") + '.jpg'
    original_image = Image.open(original_image_path)
    image = original_image.copy()

    while True:
        print("Choose an option:")
        print("1. Randomize pixels")
        print("2. Randomize RGB")
        print("3. Swap pixel blocks")
        print("4. Randomize RGB for blocks")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            pixel_randomize(image)
            print("Pixels randomized.")
        elif choice == '2':
            pixel_rgb_randomize(image)
            print("RGB randomized.")
        elif choice == '3':
            swap_pixel_blocks(image)
            print("Pixel blocks swapped.")
        elif choice == '4':
            block_rgb_randomize(image)
            print("RGB for blocks randomized.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        # Ask if the user wants to continue editing or save the edited image
        continue_choice = input("Do you want to continue editing? (y/n): ")
        if continue_choice.lower() == 'n':
            break

    # Ask if the user wants to save the final edited image
    save_choice = input("Do you want to save the edited image? (y/n): ")
    if save_choice.lower() == 'y':
        image_path = 'images/' + input("Enter the name for the edited image (including extension, e.g., 'edited_image'): ") + '.jpg'
        image.save(image_path)
        print(f"Edited image saved to {image_path}")




def pixel_randomize(image):
    pixels = image.load()
    width, height = image.size

    step_size = int(input("Enter the step size (an integer): "))
    
    for y in range(0, image.height, step_size):
        for x in range(0, image.width, step_size):
            pixels[x, y] = pixels[random.randint(0, width-1), random.randint(0, height-1)]

def pixel_rgb_randomize(image):
    pixels = image.load()
    width, height = image.size

    shift_range = int(input("Enter the shift range (an integer): "))

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r_shift = random.randint(-shift_range, shift_range)
            g_shift = random.randint(-shift_range, shift_range)
            b_shift = random.randint(-shift_range, shift_range)
            
            # Ensure the new values are within the valid range [0, 255]
            r = max(0, min(255, r + r_shift))
            g = max(0, min(255, g + g_shift))
            b = max(0, min(255, b + b_shift))
            
            pixels[x, y] = (r, g, b)

def swap_pixel_blocks(image):
    pixels = image.load()
    width, height = image.size

    block_width = int(input("Enter the block width (an integer): "))
    block_height = int(input("Enter the block height (an integer): "))

    def swap_blocks(x1, y1, x2, y2, block_width, block_height):
        for i in range(block_width):
            for j in range(block_height):
                if (x1 + i < width and y1 + j < height and x2 + i < width and y2 + j < height):
                    pixels[x1 + i, y1 + j], pixels[x2 + i, y2 + j] = pixels[x2 + i, y2 + j], pixels[x1 + i, y1 + j]

    for _ in range((width * height) // (block_width * block_height)):
        x1 = random.randint(0, width - block_width)
        y1 = random.randint(0, height - block_height)
        x2 = random.randint(0, width - block_width)
        y2 = random.randint(0, height - block_height)
        swap_blocks(x1, y1, x2, y2, block_width, block_height)

def block_rgb_randomize(image):
    pixels = image.load()
    width, height = image.size

    block_width = int(input("Enter the block width (an integer): "))
    block_height = int(input("Enter the block height (an integer): "))
    shift_range = int(input("Enter the shift range (an integer): "))

    def shift_block_rgb(x, y, block_width, block_height, shift_range):
        r_shift = random.randint(-shift_range, shift_range)
        g_shift = random.randint(-shift_range, shift_range)
        b_shift = random.randint(-shift_range, shift_range)
        
        for i in range(block_width):
            for j in range(block_height):
                if x + i < width and y + j < height:
                    r, g, b = pixels[x + i, y + j]
                    r = max(0, min(255, r + r_shift))
                    g = max(0, min(255, g + g_shift))
                    b = max(0, min(255, b + b_shift))
                    pixels[x + i, y + j] = (r, g, b)

    for x in range(0, width, block_width):
        for y in range(0, height, block_height):
            shift_block_rgb(x, y, block_width, block_height, shift_range)



if __name__ == "__main__":
    main()
