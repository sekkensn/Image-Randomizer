# Image Randomizer

This script provides a set of functions to perform various image editing operations, including randomizing pixels, randomizing RGB values, swapping pixel blocks, and randomizing RGB values for pixel blocks. The script prompts the user to select an editing option and can apply multiple edits in a single session.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Install Python from the official website: [Python.org](https://www.python.org/)
2. Install the Pillow library using pip:
    ```bash
    pip install pillow
    ```

## Usage

1. Place the image you want to edit in the `images` directory.
2. Run the script:
    ```bash
    python dm.py
    ```
3. Follow the prompts to select an editing option and make edits to the image.

## Editing Options

The script provides the following editing options:

1. **Randomize pixels**: Randomly swaps pixels within the image.
2. **Randomize RGB**: Randomly shifts the RGB values of each pixel.
3. **Swap pixel blocks**: Randomly swaps blocks of pixels within the image.
4. **Randomize RGB for blocks**: Randomly shifts the RGB values of blocks of pixels.
5. **Quit**: Exit the program.

## Functions

### `pixel_randomize(image)`

Randomizes the pixels within the image. Prompts the user for a step size, which determines how many pixels to skip when selecting pixels to swap.

### `pixel_rgb_randomize(image)`

Randomizes the RGB values of each pixel within the image. Prompts the user for a shift range, which determines the range within which the RGB values are shifted.

### `swap_pixel_blocks(image)`

Swaps blocks of pixels within the image. Prompts the user for the block width and height, which determine the size of the blocks to be swapped.

### `block_rgb_randomize(image)`

Randomizes the RGB values of blocks of pixels within the image. Prompts the user for the block width, block height, and shift range, which determine the size of the blocks and the range within which the RGB values are shifted.

## Example

Here is an example of how to use the script:

1. Place an image named `001.jpg` in the `images` directory.
2. Run the script:
    ```bash
    python dm.py
    ```
3. Enter the name of the image you want to edit (e.g., `001`).
4. Choose an editing option (e.g., `1` for randomizing pixels).
5. Follow the prompts to specify the parameters for the chosen editing option.
6. After making edits, you can choose to continue editing or save the edited image.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
